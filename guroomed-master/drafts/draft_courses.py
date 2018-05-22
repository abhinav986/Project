from django.http import HttpResponse
import simplejson as json
from .models import DraftCourse, CoursesRoles, CurriculumSection as CS, CurriculumLecture as CL
from quizzes.models import Quizzes, Questions, Answers
from courses.models import Subcategory, Language, Instructor, Tag
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
import vimeo
from django.conf import settings
from users.models import SubcategoryRoles
from django.core.mail import send_mail


# this function will assign reviewer to draft_course
@csrf_exempt
def course_assign(request, course_id):
    if request.method == 'GET':
        try:
            reviewers = []
            for reviewer in User.objects.filter(groups__name='Course Reviewer'):
                if reviewer.first_name or reviewer.last_name:
                    label = reviewer.first_name + ' ' + reviewer.last_name
                else:
                    label = reviewer.email
                reviewers.append({
                    'value' : reviewer.id,
                    'label' : label,
                })
        except Exception as e:
            return HttpResponse(json.dumps({'status':0, 'error':str(e)}))
        return HttpResponse(json.dumps({'status':1, 'reviewers':reviewers}))
            
    if request.method == 'POST':
        if not request.user.is_authenticated: #if user is not logged in
            return HttpResponse(json.dumps({'status':0, 'error':'Please Login'}))
        if 'group_id' not in request.POST:
            return HttpResponse(json.dumps({'status':0, 'error':'Group Id is not there'}))
        if int(request.POST['group_id']) == 7 or int(request.POST['group_id']) == 8:
            pass
        else:
            return HttpResponse(json.dumps({'status':0,'error':'Wrong Group ID'}))
        if 'user_ids[]' not in request.POST:
            return HttpResponse(json.dumps({'status':0, 'error':'User Id is not there'}))
        if not (request.user.groups.filter(id=7).exists() or request.user.groups.filter(id=5).exists() or request.user.groups.filter(id=6).exists()):
            return HttpResponse(json.dumps({'status':0,'error':'You are not authorized user'}))
        try:
            draft = DraftCourse.objects.get(id=course_id)
            group = Group.objects.get(id=request.POST['group_id']) #7, 8
            reviewers_selected = []
            for user_id in request.POST.getlist('user_ids[]'):
                user = User.objects.get(id=user_id)
                if not user.groups.filter(id=request.POST['group_id']).exists():
                    return HttpResponse(json.dumps({'status':0,'error':'User does not have this role'}))
                cr = CoursesRoles(user_id=user, course_draft_id=draft, role_type=group)
                cr.save()
                send_mail(
                    'Guroomed - New Course for Review',
                    'New Course Assigned for Review - '+ draft.title,
                    'no-reply@guroomed.com',
                    [user.email],
                    fail_silently=False,
                )
                if not (user.first_name and user.last_name):
                    name =  user.email
                else:
                    name =  user.first_name+ ' ' + user.last_name
                reviewers_selected.append({
                    'value' : user.id,
                    'label' : name,
                })
        except Exception as e:
            return HttpResponse(json.dumps({'status':0,'error':str(e)}))
        return HttpResponse(json.dumps({'status':1,'msg':'Course - '+ draft.title +' has been Assigned to reviewers'}))
        # return HttpResponse(json.dumps({'status':1,'msg':'Course - '+ draft.title +' has been Assigned to reviewers' + str(reviewers_selected)}))
    else:
        return HttpResponse(json.dumps({'status':0,'msg':'Wrong Method'}))
        

# To let instructor to create new draft_course ( just title will be added )
@csrf_exempt
def create(request):
    if request.method == 'GET':
        sub_cats = []
        for sub_cat in Subcategory.objects.all():
            sub_cats.append({
                'value' : sub_cat.id,
                'label' : sub_cat.name,
            })
        tags = []
        for tag in Tag.objects.all():
            tags.append({
                'value' : tag.id,
                'label' : tag.name,
            })
        languages = []
        for lang in Language.objects.all():
            languages.append({
                'value' : lang.id,
                'label' : lang.name,
            })
        levels = [
            {'value': 'All' , 'label': 'All'},
            {'value': 'Beginner' , 'label': 'Beginner'},
            {'value': 'Intermediate' , 'label': 'Intermediate'},
            {'value': 'Expert' , 'label': 'Expert'}
        ]
        if 'id' in request.GET:
            draft = getDraft(request, request.GET['id'])
        else:
            draft = None
        return HttpResponse(json.dumps({
            'sub_cats': sub_cats,
            'tags': tags,
            'languages': languages,
            'levels': levels,
            'draft': draft
        }))

    if request.method == 'POST':
        if not request.user.is_authenticated: #if user is not logged in
            return HttpResponse(json.dumps({'status':0, 'error':'Please Login'}))
        if not request.user.groups.filter(name='Instructor').exists():
            return HttpResponse(json.dumps({'status':0, 'error':'Not a valid user'}))
        try:
            instructor = Instructor.objects.get(user_id=request.user.id)
        except Instructor.DoesNotExist:
            return HttpResponse(json.dumps({'status':0, 'error':'Need to create instructor record'}))
        if 'course_title' not in request.POST:
            return HttpResponse(json.dumps({'status':0, 'error':'Please enter Title'}))
        try:
            draft = DraftCourse(title = request.POST['course_title'], price=0)
            draft.save()
            draft.instructor.add(instructor.id)
        except Exception as e:
            return HttpResponse(json.dumps({'status':0, 'error':str(e)}))
        return HttpResponse(json.dumps({'status':1, 'course_id':draft.id, 'course_title':draft.title}))
    else:
        return HttpResponse(json.dumps({'status':0, 'error':'Please use POST method'}))


# to add the basic information of draft_course
@csrf_exempt
def add_basics(request, id):
    if request.method == 'POST':
        if not request.user.is_authenticated: #if user is not logged in
            return HttpResponse(json.dumps({'status':0, 'error':'Please Login'}))
        try:
            draft = DraftCourse.objects.get(id=id)
        except DraftCourse.DoesNotExist:
            return HttpResponse(json.dumps({'status':0, 'error':'Course does not exist'}))
        # if request.user.id != draft.user.id:
        #     return HttpResponse(json.dumps({'status':0, 'error':'Not a valid user'}))
        if 'course_title' not in request.POST:
            return HttpResponse(json.dumps({'status':0, 'error':'Please enter Title'}))
        if 'course_subtitle' not in request.POST:
            subtitle = None
        else:
            subtitle = request.POST['course_subtitle']
        if 'course_price' not in request.POST:
            price = None
        else:
            price = request.POST['course_price']
        if 'category' not in request.POST:
            return HttpResponse(json.dumps({'status':0, 'error':'Select Subcategory'}))
        if 'language' not in request.POST:
            return HttpResponse(json.dumps({'status':0, 'error':'Select Language'}))
        if 'level' not in request.POST:
            level = None
        else:
            level = request.POST['level']

        if 'preview_video' not in request.FILES:
            preview_video = None
        else:
            v = vimeo.VimeoClient(
                key=settings.VIMEO_CLIENT_ID,
                token=settings.VIMEO_ACCESS_TOKEN,
                secret=settings.VIMEO_CLIENT_SECRET
            )
            video_uri = v.upload(request.FILES['preview_video'].temporary_file_path())
            v.patch(video_uri, data={'name': request.FILES['preview_video'].name})
            preview_video = video_uri[8:]

        if 'photo_link' not in request.FILES:
            photo_link = None
        else:
            try:
                uploaded_file = request.FILES['photo_link']
                with open(settings.MEDIA_ROOT+'/'+uploaded_file.name, 'wb+') as destination:
                    for chunk in uploaded_file.chunks():
                            destination.write(chunk)
                photo_link = settings.MEDIA_URL+uploaded_file.name
            except Exception as e:
                return HttpResponse(json.dumps({'status':0, 'error':str(e)}))

        try:
            sub_cat = Subcategory.objects.get(id=request.POST['category'])
        except Subcategory.DoesNotExist:
            return HttpResponse(json.dumps({'status':0, 'error':'Wrong Subcategory Id'}))
        try:
            language = Language.objects.get(id=request.POST['language'])
        except Language.DoesNotExist:
            return HttpResponse(json.dumps({'status':0, 'error':'Wrong Language Id'}))

        try:
            draft.title = request.POST['course_title']
            draft.subtitle = subtitle
            draft.price = price
            draft.course_subcategory = sub_cat
            draft.course_language = language
            draft.preview_image_url = photo_link
            draft.preview_video_url = preview_video
            draft.level = level
            draft.save()
        except Exception as e:
            return HttpResponse(json.dumps({'status':0, 'error':str(e)}))
        return HttpResponse(json.dumps({'status':1, 'course_id':draft.id, 'msg':'Updated Course - '+draft.title}))
    else:
        return HttpResponse(json.dumps({'status':0, 'error':'Please use POST method'}))


# to add the goals of draft_course
@csrf_exempt
def add_goals(request, id):
    if request.method == 'POST':
        if not request.user.is_authenticated: #if user is not logged in
            return HttpResponse(json.dumps({'status':0, 'error':'Please Login'}))
        try:
            draft = DraftCourse.objects.get(id=id)
        except DraftCourse.DoesNotExist:
            return HttpResponse(json.dumps({'status':0, 'error':'Course does not exist'}))
        # if request.user.id != draft.user.id:
        #     return HttpResponse(json.dumps({'status':0, 'error':'Not a valid user'}))
        if 'learnGoal' not in request.POST:
            what_will_i_learn = None
        else:
            what_will_i_learn = request.POST['learnGoal']
        if 'targetStudent' not in request.POST:
            targetStudent = None
        else:
            targetStudent = request.POST['targetStudent']
        if 'knowledgeRequired' not in request.POST:
            knowledgeRequired = None
        else:
            knowledgeRequired = request.POST['knowledgeRequired']
        try:
            draft.what_will_i_learn = what_will_i_learn
            draft.requirements = knowledgeRequired
            draft.description = targetStudent
            draft.save()
        except Exception as e:
            return HttpResponse(json.dumps({'status':0, 'error':str(e)}))
        return HttpResponse(json.dumps({'status':1, 'course_id':draft.id, 'msg':'Updated Course - '+draft.title}))
    else:
        return HttpResponse(json.dumps({'status':0, 'error':'Please use POST method'}))


# to add curriculum section into draft_course
@csrf_exempt
def add_sections(request, id):
    if request.method == 'POST':
        if not request.user.is_authenticated: #if user is not logged in
            return HttpResponse(json.dumps({'status':0, 'error':'Please Login'}))
        try:
            draft = DraftCourse.objects.get(id=id)
        except DraftCourse.DoesNotExist:
            return HttpResponse(json.dumps({'status':0, 'error':'Course does not exist'}))
        if 'title' not in request.POST:
            return HttpResponse(json.dumps({'status':0, 'error':'Please Enter Title'}))
        if 'order_num' not in request.POST:
            return HttpResponse(json.dumps({'status':0, 'error':'Please Enter Order Number'}))
        for cs in CS.objects.all().filter(course_draft_id = id):
            if cs.order_num == request.POST['order_num']:
                return HttpResponse(json.dumps({'status':0, 'error':'Please change the order'}))
        if 'no_lectures' not in request.POST:
            return HttpResponse(json.dumps({'status':0, 'error':'Please Enter Number of Lectures'}))
        if 'duration' not in request.POST:
            return HttpResponse(json.dumps({'status':0, 'error':'Please Enter Duration'}))
        try:
            cs = CS(course_draft_id=draft, title=request.POST['title'], order_num=request.POST['order_num'], no_lectures=request.POST['no_lectures'], duration=request.POST['duration'])
            cs.save()
        except Exception as e:
            return HttpResponse(json.dumps({'status':0, 'error':str(e)}))
        return HttpResponse(json.dumps({'status':1, 'section_id':cs.id, 'msg':'Added Section - '+cs.title}))
    if request.method == 'DELETE':
        try:
            cs = CS.objects.get(id=id)
            title = cs.title
            cs.delete()
        except CS.DoesNotExist:
            return HttpResponse(json.dumps({'status':0, 'error':'Wrong Section Id'}))
        return HttpResponse(json.dumps({'status':1, 'section_id':cs.id, 'msg':'Deleted Section - '+title}))
    else:
        return HttpResponse(json.dumps({'status':0, 'error':'Wrong method'}))


# to add curriculum lectures into draft_course
@csrf_exempt
def add_lectures(request, id):
    if request.method == 'POST':
        if not request.user.is_authenticated: #if user is not logged in
            return HttpResponse(json.dumps({'status':0, 'error':'Please Login'}))
        if 'video' not in request.FILES:
            return HttpResponse(json.dumps({'status':0, 'error':'Please upload the video'}))
        # if 'section_id' not in request.POST:
            # return HttpResponse(json.dumps({'status':0, 'error':'Section id is not there'}))
        if 'title' not in request.POST:
            return HttpResponse(json.dumps({'status':0, 'error':'Please enter Title'}))
        if 'order_num' not in request.POST:
            return HttpResponse(json.dumps({'status':0, 'error':'Please enter order'}))
        if 'lecture_type' not in request.POST:
            return HttpResponse(json.dumps({'status':0, 'error':'Please enter lecture type'}))
        if 'description' not in request.POST:
            description = ''
        else:
            description = request.POST['description']
        try:
            v = vimeo.VimeoClient(
                key=settings.VIMEO_CLIENT_ID,
                token=settings.VIMEO_ACCESS_TOKEN,
                secret=settings.VIMEO_CLIENT_SECRET
            )
            video_uri = v.upload(request.FILES['video'].temporary_file_path())
            v.patch(video_uri, data={'name': request.FILES['video'].name})
            video_uri = video_uri[8:]
        except Exception as e:
            return HttpResponse(json.dumps({'status':0, 'error':str(e)}))
        try:
            section = CS.objects.get(id=id)
        except CS.DoesNotExist:
            return HttpResponse(json.dumps({'status':0, 'error':'Wrong section id'}))
        try:
            cl = CL()
            cl.curriculum_section_id=section
            cl.title=request.POST['title']
            cl.description=description
            cl.preview_url=video_uri
            cl.video_url=video_uri
            cl.order_num=request.POST['order_num']
            cl.lecture_type=request.POST['lecture_type']
            cl.save()
        except Exception as e:
            return HttpResponse(json.dumps({'status':0, 'error':str(e)}))
        return HttpResponse(json.dumps({'status':1, 'lecture_id':cl.id, 'msg':'Lecture created - '+cl.title}))
        if request.method == 'DELETE':
            try:
                cl = CL.objects.get(id=id)
                title = cl.title
                cl.delete()
            except CL.DoesNotExist:
                return HttpResponse(json.dumps({'status':0, 'error':'Wrong Lecture Id'}))
            return HttpResponse(json.dumps({'status':1, 'section_id':cs.id, 'msg':'Deleted Lecture - '+title}))
        else:
            return HttpResponse(json.dumps({'status':0, 'error':'Wrong method'}))


# to get the all curriculum data of a draft_course
@csrf_exempt
def get_curriculum(request, id):
    if request.method == 'GET':
        if not request.user.is_authenticated: #if user is not logged in
            return HttpResponse(json.dumps({'status':0, 'error':'Please Login'}))
        try:
            draft = DraftCourse.objects.get(id=id)
        except DraftCourse.DoesNotExist:
            return HttpResponse(json.dumps({'status':0, 'error':'Course does not exist'}))
        try:
            curriculumSec = []
            for section in CS.objects.all().filter(course_draft_id=draft):
                curriculumLect = []
                curriculumQuiz = []
                
                for lecture in CL.objects.all().filter(curriculum_section_id=section.id):
                    curriculumLect.append({
                        'title':lecture.title,
                        'description':lecture.description,
                        'preview_url':lecture.preview_url,
                        'video_url':lecture.video_url,
                        'order_num':lecture.order_num,
                        'lecture_type':lecture.lecture_type,
                    })
                for quiz in Quizzes.objects.filter(course_section_id=section.id):
                    quizQuestion = []
                    for quiz_question in Questions.objects.filter(quiz_id=quiz.id):
                        quizAnswer = []
                        for ans in Answers.objects.filter(question_id=quiz_question.id):
                            quizAnswer.append({
                            'id':ans.id,
                            'answer':ans.answer,
                            'is_correct':ans.is_correct,
                            'order':ans.order
                            })
                        quizQuestion.append({
                            'id':quiz_question.id,
                            'content':quiz_question.content,
                            'answer':quizAnswer
                            })
                    curriculumQuiz.append({
                        'id':quiz.id,
                        'title':quiz.title,
                        'description':quiz.description,
                        'quizQuestion':quizQuestion
                        })

                curriculumSec.append({
                    'id':section.id,
                    'title':section.title,
                    'curriculumLect':curriculumLect,
                    'curriculumQuiz':curriculumQuiz,
                    'order_num':section.order_num,
                    'no_lectures':section.no_lectures,
                    'duration':str(section.duration),
                })
        except Exception as e:
            return HttpResponse(json.dumps({'status':0, 'error':str(e)}))
        return HttpResponse(json.dumps({'status':1, 'curriculum':curriculumSec}))
    else:
        return HttpResponse(json.dumps({'status':0, 'error':'Please use GET method'}))


# to let the instructor submit the draft_course. After submitting draft_course, request will go to manager for approval
@csrf_exempt
def draft_submit(request, id):
    if request.method == 'POST':
        if not request.user.is_authenticated: #if user is not logged in
            return HttpResponse(json.dumps({'status':0, 'error':'Please Login'}))
        try:
            draft = DraftCourse.objects.get(id=id)
        except DraftCourse.DoesNotExist:
            return HttpResponse(json.dumps({'status':0, 'error':'Course does not exist'}))
        managers_sub = []    
        try:
            managers_sub = SubcategoryRoles.objects.filter(subcategory_id = draft.course_subcategory.id)
        except SubcategoryRoles.DoesNotExist:
            return HttpResponse(json.dumps({'status':0,'error':'No Manager Found in this Subcategory'}))
        flag = 0
        for inst in draft.instructor.all():#if loggedin user is not the course instructor
            if request.user.id == inst.user_id.id:
                flag = 1
                break
        if flag == 0:
            return HttpResponse(json.dumps({'status':0, 'error':'Not a valid user'}))
        draft.is_reviewed = 0
        draft.save()
        group = Group.objects.get(id=7)
        #get all managers of subcategory same as draft course subcategory
        for manager_sub in managers_sub:
            #assign course to the manager
            cr = CoursesRoles(user_id=manager_sub.user_id, course_draft_id=draft, role_type=group)
            cr.save()            
            send_mail(
                'Guroomed - New Course Submission',
                'New Course Submission - '+ draft.title,
                'no-reply@guroomed.com',
                [manager_sub.user_id.email],
                fail_silently=False,
            )
        return HttpResponse(json.dumps({'status':1, 'course_id':draft.id, 'msg':'Submitted Course for review - '+draft.title}))
    else:
        return HttpResponse(json.dumps({'status':0, 'error':'Please use POST method'}))


# to get the draft_course information
def getDraft(request, id):
    try:
        draft = DraftCourse.objects.get(id=id)
    except DraftCourse.DoesNotExist:
        context = {'status':0, 'error':'Course does not exist'}
        return context
    if draft.course_subcategory:
        subcategory = {'value':draft.course_subcategory.id, 'label': draft.course_subcategory.name}
    else:
        subcategory = None
    if draft.course_language:
        language = {'value':draft.course_language.id, 'label': draft.course_language.name}
    else:
        language = None
    if draft.level == None:
        level = None
    else:
        level = {'value':draft.level, 'label':draft.level}
    try:
        instructors = []
        print(draft.instructor.all())
        for inst in draft.instructor.all():
            if not (inst.user_id.first_name or inst.user_id.last_name):
                instructors.append(inst.user_id.email)
            else:
                instructors.append(inst.user_id.first_name +' '+ inst.user_id.last_name )
        draft_content = {
            'course_id' : draft.id,
            'course_title' : draft.title,
            'course_subtitle' : draft.subtitle,
            'course_price' : draft.price,
            'subcategory' : subcategory,
            'language' : language,
            'level' : level,
            'instructor' : instructors,
            'preview_image_url' : draft.level,
            'preview_video_url' : draft.preview_video_url,
            'what_will_i_learn' : draft.what_will_i_learn,
            'knowledgeRequired' : draft.requirements,
            'targetStudent' : draft.description,
            'is_draft' : draft.is_draft,
            'is_reviewed' : draft.is_reviewed,
            'status' : draft.status,
            'created_at' : str(draft.created_at),
            'updated_at' : str(draft.updated_at),
        }
    except Exception as e:
        context = {'status':0, 'error':str(e)}
        return context
    return draft_content
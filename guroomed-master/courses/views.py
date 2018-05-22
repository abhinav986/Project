from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from .models import Subcategory
from .models import Language
from .models import Course, Instructor, Tag
from django.http import HttpResponse
import jwt
import simplejson as json
from . import curriculumsection as cur
from guroomed.models import UserCourses
from guroomed.all_users import fupload
from decimal import Decimal
from elasticsearch import Elasticsearch
from datetime import datetime
# from .forms import CourseForm


# to show the listing of all the courses
def index(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'courses/courseslisting.html', context)

# to show the form to add the course
def create(request):
    sub_cats = Subcategory.objects.all()
    instructors = Instructor.objects.all()
    tags = Tag.objects.all()
    languages = Language.objects.all()
    context = {'sub_cats': sub_cats, 'users': instructors, 'tags': tags, 'languages': languages,}
    return render(request, 'courses/create.html', context)

# to add the course in database
def store(request):
    # Creating a form to add an article.
    # if request.method == 'POST':
    #     form = CourseForm(request.POST)
    #     if form.is_valid():
    #         return redirect('/api/courses/')
    # else:
    #     form = CourseForm()
    # return render(request, 'courses/create.html', {'form': form})    

    if 'course_subcategory_id' not in request.POST:
        return HttpResponse(json.dumps({'status':0, 'error':'Select Subcategory'}))
    if 'user_id[]' not in request.POST:
        return HttpResponse(json.dumps({'status':0, 'error':'Select Instructor'}))
    if 'course_language_id' not in request.POST:
        return HttpResponse(json.dumps({'status':0, 'error':'Select Language'}))
    if request.POST['title'] == '':
        return HttpResponse(json.dumps({'status':0, 'error':'Enter Title'}))

    try:
        sub_cat = Subcategory.objects.get(id=request.POST['course_subcategory_id'])
    except Subcategory.DoesNotExist:
        return HttpResponse(json.dumps({'error':'Wrong Subcategory Id'}))
    try:
        language = Language.objects.get(id=request.POST['course_language_id'])
    except Language.DoesNotExist:
        return HttpResponse(json.dumps({'error':'Wrong Language Id'}))

    instructors = []
    for user_id in request.POST.getlist('user_id[]'):
        try:
            instructors.append(Instructor.objects.get(id=user_id))
        except Instructor.DoesNotExist:
            return HttpResponse(json.dumps({'error':'Wrong Instructor Id'}))

    tags = []
    for t in request.POST.getlist('tags[]'):
        try:
            tags.append(Tag.objects.get(id=t))
        except Tag.DoesNotExist:
            return HttpResponse(json.dumps({'error':'Wrong Tag Id'}))

    try:
        params = request.POST
        course = Course()
        course.course_subcategory_id = sub_cat
        course.course_language_id = language
        course.title = params.get('title')
        course.subtitle = params.get('subtitle')

        if params.get('ratings'):
            course.ratings = params.get('ratings')
        if params.get('rating_count'):
            course.rating_count = params.get('rating_count')
        if params.get('students_enrolled'):
            course.students_enrolled = params.get('students_enrolled')
        if params.get('what_will_i_learn'):
            course.what_will_i_learn = params.get('what_will_i_learn')
        if params.get('description'):
            course.description = params.get('description')
        if params.get('preview_video_url'):
            course.preview_video_url = params.get('preview_video_url')
        if params.get('requirements'):
            course.requirements = params.get('requirements')
        if params.get('price'):
            course.price = params.get('price')
        if params.get('discount'):
            course.discount = params.get('discount')
        if params.get('no_lectures'):
            course.no_lectures = params.get('no_lectures')
        if params.get('no_hours'):
            course.no_hours = params.get('no_hours')
        if params.get('level'):
            course.level = params.get('level')
        if params.get('slug'):
            course.slug = params.get('slug')

        if 'preview_image_url' not in request.FILES:
            course.preview_image_url = ''
        else :
            course.preview_image_url = fupload(request.FILES['preview_image_url'])
        course.save()
    except Exception as e:
        return HttpResponse(json.dumps({'status':0, 'error':str(e)}))
    print(tags)
    try:
        for instructor in instructors:
            course.instructor_id.add(instructor.id)
        for tag in tags:
            course.tags.add(tag)
        print(course.tags)
    except Exception as e:
        return HttpResponse(json.dumps({'status':0, 'error':str(e)}))

    suggestions = []
    for word in course.title.split(' '):
        suggestions.append(word)
    es = Elasticsearch()
    tagname = []
    for tag in course.tags.all():
        tagname.append(tag.name)
    instructors_names = []
    for instructor in course.instructor_id.all():
        instructors_names.append(instructor.user_id.first_name +' '+ instructor.user_id.last_name)

    features = []
    for f in request.POST.getlist('features[]'):
        features.append(f)

    try:
        if course.description == None:
            description = ''
        else:
            description = course.description[:200]
        doc={
            'category': course.course_subcategory_id.course_category_id.name,
            'subcategory': course.course_subcategory_id.name,
            'tags': tagname,
            'topics': course.no_lectures,
            'label': 'New',
            'coursename': course.title,
            'hours': course.no_hours,
            'image_url': course.preview_image_url,
            'instructor': instructors_names,
            'offer': course.discount,
            'price': course.price,
            'rating_score': course.ratings,
            'students': course.students_enrolled,
            'short_description': description,
            'difficulty_level': course.level,
            'languages': course.course_language_id.name,
            'features': features,
            # 'course_link': ''course.id,
            'no_of_lectures': course.no_lectures,
            'subtitles': course.subtitle,
            'no_of_reviews': course.rating_count,
            'created_at': datetime.now(),
            'searchSuggest' : {
               "input": suggestions,
               # "output": request.POST['coursename']
            }
        }
        res = es.index(index='course', doc_type='courses', id=course.id, body=doc)
    except Exception as e:
        return HttpResponse(json.dumps({'status':0, 'error':str(e)}))
    return redirect('/api/courses/')

# to show the form to edit the course
def edit(request, id):
    course = Course.objects.get(id=id)
    sub_cats = Subcategory.objects.all()
    users = Instructor.objects.all()
    languages = Language.objects.all()
    context = {'course': course, 'sub_cats': sub_cats, 'users': users, 'languages': languages,}
    return render(request, 'courses/edit.html', context)

# to display the course details in frontend
def frontend_show(request, id):
    course = Course.objects.get(id=id)

    allTags = Tag.objects.all()
    tags = []
    for tag in course.tags.all():
        tags.append(tag.name)

    instructors = []
    for instructor in course.instructor_id.all():
        instructors.append({
            'first_name' : instructor.user_id.first_name,
            'last_name' : instructor.user_id.last_name
        })

    curriculums = cur.show(request, course.id)
    # return HttpResponse(curriculums)
    return HttpResponse(json.dumps({
        'id' : course.id,
        'title' : course.title,
        'subtitle' : course.subtitle,
        'course_subcategory_name' : course.course_subcategory_id.name,
        'course_language_name' : course.course_language_id.name,
        'instructors' : instructors,
        'description' : course.description,
        'requirements' : course.requirements,
        'what_will_i_learn' : course.what_will_i_learn,
        'students_enrolled' : course.students_enrolled,
        'price' : course.price,
        'discount' : course.discount,
        'ratings' : course.ratings,
        'rating_count' : course.rating_count,
        'preview_video_url' : course.preview_video_url,
        'preview_image_url' : course.preview_image_url,
        'no_lectures' : course.no_lectures,
        'level' : course.level,
        'tags' : tags,
        'no_hours' : course.no_hours,
        'updated_at' : str(course.updated_at),
        'curriculum' : curriculums,
    }))

# to view the course in admin panel
def show(request, id):
    course = Course.objects.get(id=id)
    sub_cats = Subcategory.objects.get(id=course.course_subcategory_id.id)
    instructors = course.instructor_id.all()
    tags = course.tags.all()
    languages = Language.objects.all()
    context = {'course': course, 'sub_cats': sub_cats, 'instructors': instructors, 'tags': tags, 'languages': languages,}
    return render(request, 'courses/singlecourse.html', context)

# to update the course
def update(request, id):
    sub_cat = get_object_or_404(Subcategory, pk=request.POST['course_subcategory_id'])
    language = get_object_or_404(Language, pk=request.POST['course_language_id'])
    user = get_object_or_404(Instructor, pk=request.POST['user_id'])
    course = Course.objects.get(id=id)
    course.course_subcategory_id = sub_cat
    course.course_language_id = language
    course.instructor_id = user
    course.title = request.POST['title']
    # course.subtitle = request.POST['subtitle']
    course.ratings = request.POST['ratings']
    course.rating_count = request.POST['rating_count']
    course.students_enrolled = request.POST['students_enrolled']
    course.what_will_i_learn = request.POST['what_will_i_learn']
    course.description = request.POST['description']
    course.requirements = request.POST['requirements']
    course.discount = request.POST['discount']
    course.save()
    return redirect('/api/courses/')

# to delete the course
def delete(request, id):
    try:
        course = Course.objects.get(id=id)
        course.delete()
        es = Elasticsearch()
        es.delete(index='course', doc_type='courses', id=id, ignore=[404,400])
    except Exception as e:
        return HttpResponse(json.dumps({'status':0, 'error':str(e)}))
    return redirect('/api/courses/')

# to get the information of all the courses purchased by a student
def mycourses(request, id):
    myCourses = UserCourses.objects.all().filter(user_id=id)
    courses = []
    for mc in myCourses:
        course = Course.objects.get(id=mc.course_id.id)
        courses.append({
            'id' : course.id,
            'preview_image_url' : course.preview_image_url,
            'title' : course.title,
            'description' : course.description,
            'progress' : '30%',
            'rating' : 3.4,
        })
    return HttpResponse(json.dumps({'courses':courses}))

# to get all the data of curriculum
def getCurriculum(request, id):
    curriculums = cur.show(request, id)
    return HttpResponse(json.dumps({
        'curriculum' : curriculums,
    }))
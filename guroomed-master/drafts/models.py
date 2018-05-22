from django.db import models
from django.contrib.auth.models import User, Group
from courses.models import Subcategory, Language, Instructor, Tag

class DraftCourse(models.Model):
    course_subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True)
    course_language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    instructor = models.ManyToManyField(Instructor)
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=250, null=True)
    ratings = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    rating_count = models.IntegerField(null=True)
    students_enrolled = models.IntegerField(null=True)
    what_will_i_learn = models.TextField(null=True)
    requirements = models.TextField(null=True)
    description = models.TextField(null=True)
    preview_video_url = models.FilePathField(max_length=255, null=True)
    preview_image_url = models.FilePathField(max_length=255, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    discount = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    no_lectures = models.IntegerField(null=True)
    no_hours = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    slug = models.SlugField(unique=True, null=True)
    tags = models.ManyToManyField(Tag)
    labels = ( ('New', 'New'), ('Bestseller', 'Bestseller'))
    label = models.CharField(max_length=20, choices=labels, default='New', null=True)
    levels = ( ('Beginner', 'Beginner'), ('Expert', 'Expert'), ('All', 'All'), ('Intermediate', 'Intermediate'), )
    level = models.CharField(max_length=20, choices=levels, default='All', null=True)
    is_draft = models.BooleanField(default=1)
    is_reviewed = models.NullBooleanField() # null - yet to be submitted , 0 - submitted, 1 - not reviewed
    status = models.NullBooleanField() #null - processing, 0 - rejected, 1 - accpted

    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)


class CoursesRoles(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	course_draft_id = models.ForeignKey(DraftCourse, on_delete=models.CASCADE)
	role_type = models.ForeignKey(Group, on_delete=models.CASCADE)
	created_at = models.DateField(auto_now=True)
	updated_at = models.DateField(auto_now=True)


class ReasonsRejected(models.Model):
	text = models.CharField(max_length=100)
	types = ( ('Course Manager', 'Course Manager'), ('Course Reviewer', 'Course Reviewer') )
	type = models.CharField(max_length=20,  choices=types)


class ReviewedCourses(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	course_draft_id = models.ForeignKey(DraftCourse, on_delete=models.CASCADE)
	comments = models.CharField(max_length=300)
	status = models.NullBooleanField()
	reason_rejected = models.ForeignKey(ReasonsRejected, on_delete=models.CASCADE, null=True)
	created_at = models.DateField(auto_now=True)
	updated_at = models.DateField(auto_now=True)


class ApprovedCourses(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	course_draft_id = models.ForeignKey(DraftCourse, on_delete=models.CASCADE)
	comments = models.CharField(max_length=300)
	status = models.NullBooleanField()
	reason_rejected = models.ForeignKey(ReasonsRejected, on_delete=models.CASCADE, null=True)
	created_at = models.DateField(auto_now=True)
	updated_at = models.DateField(auto_now=True)


# class Include(models.Model):
#     course_draft_id = models.ForeignKey(DraftCourse, on_delete=models.CASCADE)
#     hours_on_demand = models.IntegerField(3, null=True)
#     supplemental_resources = models.IntegerField(3, null=True)
#     lifetime_access = models.NullBooleanField()
#     access_on_mobile = models.NullBooleanField()
#     certificate = models.NullBooleanField()

class CurriculumSection(models.Model):
    course_draft_id = models.ForeignKey(DraftCourse, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    order_num = models.IntegerField(3)
    no_lectures = models.IntegerField(3)
    duration = models.DurationField()

class CurriculumLecture(models.Model):
    curriculum_section_id = models.ForeignKey(CurriculumSection, on_delete=models.CASCADE)
    lecture_types = ( ('Video', 'Video'), ('Quiz', 'Quiz'), ('3D-Model', '3D-Model'), ('None', 'None') )
    lecture_type = models.CharField(max_length=20, choices=lecture_types, default='None')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1500)
    preview_url = models.CharField(max_length=255, null=True)
    video_url = models.CharField(max_length=255)
    order_num = models.IntegerField(3)
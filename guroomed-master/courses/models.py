from django.db import models
from django.contrib.auth.models import User, Group


class Category(models.Model):
    name = models.CharField(unique=True, max_length=30)


class Subcategory(models.Model):
    course_category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(unique=True, max_length=30)


class Language(models.Model):
    name = models.CharField(unique=True, max_length=20)


class Instructor(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    students = models.IntegerField(6)
    reviews = models.IntegerField(5)
    courses = models.IntegerField(3)


class Tag(models.Model):
    name = models.CharField(max_length=30)

    
class Course(models.Model):
    course_subcategory_id = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    course_language_id = models.ForeignKey(Language, on_delete=models.CASCADE)
    instructor_id = models.ManyToManyField(Instructor)
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

    b = 'Beginner'
    e = 'Expert'
    a = 'All'
    i = 'Intermediate'
    levels = ( (b, b), (e, e), (a, a), (i, i), )
    level = models.CharField(max_length=20, choices=levels, default=a, null=True)

    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.course_subcategory_id + "-" + self.title

# class Subtitles(models.Model):
#     course_id = models.ForeignKey(Course)
#     languages = models.ManyToManyField(Language)


class Include(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    hours_on_demand = models.IntegerField(3)
    supplemental_resources = models.IntegerField(3)
    lifetime_access = models.BooleanField()
    access_on_mobile = models.BooleanField()
    certificate = models.BooleanField()


class CurriculumSection(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
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
 

class StudentReview(models.Model):
    course_id = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_stars = models.IntegerField(1)
    about_the_course = models.CharField(max_length=500)
    about_the_instructor = models.CharField(max_length=500)
    how_course_can_improved = models.CharField(max_length=500)
    review = models.TextField()


class StudentReviewVote(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    review_id = models.ForeignKey(StudentReview, on_delete=models.CASCADE)
    like = models.BooleanField()
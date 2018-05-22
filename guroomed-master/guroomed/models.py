from django.db import models
import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import Group, User
from courses.models import Language, CurriculumLecture, Course


class UserInfo(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
    headline = models.CharField(max_length=120, null=True)
    biography = models.CharField(max_length=1600, null=True)
    language = models.ForeignKey(Language, null=True, on_delete=models.CASCADE)
    website_link = models.FilePathField(max_length=255, null=True)
    gplus_link = models.FilePathField(max_length=50, null=True)
    twitter_link = models.FilePathField(max_length=50, null=True)
    facebook_link = models.FilePathField(max_length=50, null=True)
    linkedin_link = models.FilePathField(max_length=50, null=True)
    youtube_link = models.FilePathField(max_length=50, null=True)
    photo_link = models.FilePathField(max_length=50, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by', null=True)


class InProgress(models.Model):
    courses_lecture_id = models.ForeignKey(CurriculumLecture, on_delete=models.CASCADE)
    watching_video_duration = models.DurationField()
    date_started = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class UserCourses(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    type_choices = (('taught','taught'),('learned','learned'))
    taught_learned = models.CharField(max_length=8, choices=type_choices, null=True)
    is_favourite = models.BooleanField()
    in_progress = models.ForeignKey(InProgress, null=True, on_delete=models.CASCADE)


class UserPrivacy(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    hide_search_engine = models.BooleanField()
    hide_courses = models.BooleanField()


class NotificationTypes(models.Model):
    types = models.CharField(max_length=150)


class UserNotification(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_id = models.ForeignKey(NotificationTypes, on_delete=models.CASCADE)
    

class UserCart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
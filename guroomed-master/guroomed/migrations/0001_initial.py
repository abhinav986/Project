# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-29 06:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watching_video_duration', models.TimeField()),
                ('date_started', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('courses_lecture_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.CurriculumLecture')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='UserCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taught_learned', models.CharField(choices=[('taught', 'taught'), ('learned', 'learned')], max_length=8, null=True)),
                ('is_favourite', models.BooleanField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
                ('in_progress', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='guroomed.InProgress')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=120)),
                ('biography', models.CharField(max_length=1600)),
                ('website_link', models.FilePathField(max_length=255)),
                ('gplus_link', models.FilePathField(max_length=50)),
                ('twitter_link', models.FilePathField(max_length=50)),
                ('facebook_link', models.FilePathField(max_length=50)),
                ('linkedin_link', models.FilePathField(max_length=50)),
                ('youtube_link', models.FilePathField(max_length=50)),
                ('photo_link', models.FilePathField(max_length=50)),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Language')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guroomed.NotificationTypes')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserPrivacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hide_search_engine', models.BooleanField()),
                ('hide_courses', models.BooleanField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

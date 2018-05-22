# Generated by Django 2.0.2 on 2018-04-28 05:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('guroomed', '0003_usercart'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='biography',
            field=models.CharField(max_length=1600, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='facebook_link',
            field=models.FilePathField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='gplus_link',
            field=models.FilePathField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='headline',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='linkedin_link',
            field=models.FilePathField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='photo_link',
            field=models.FilePathField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='twitter_link',
            field=models.FilePathField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='website_link',
            field=models.FilePathField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='youtube_link',
            field=models.FilePathField(max_length=50, null=True),
        ),
    ]

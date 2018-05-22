# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-26 12:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20180213_1613'),
        ('paywithpaypal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='course_id',
        ),
        migrations.AddField(
            model_name='ordercourse',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paywithpaypal.Order'),
        ),
    ]

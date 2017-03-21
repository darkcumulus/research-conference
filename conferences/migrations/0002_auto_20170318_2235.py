# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 14:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='abstract_deadline',
            field=models.DateField(default=datetime.datetime(2017, 4, 2, 14, 35, 7, 286930, tzinfo=utc), verbose_name='Deadline of Abstract Submission'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2017, 4, 19, 14, 35, 7, 286930, tzinfo=utc), verbose_name='Date Ended'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='paper_deadline',
            field=models.DateField(default=datetime.datetime(2017, 4, 7, 14, 35, 7, 287930, tzinfo=utc), verbose_name='Deadline of Paper Submission'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2017, 4, 17, 14, 35, 7, 286930, tzinfo=utc), verbose_name='Date Started'),
        ),
    ]

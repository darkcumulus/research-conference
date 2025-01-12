# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-09 02:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("conferences", "0017_auto_20170424_1645"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                ("slug", models.SlugField(blank=True, null=True)),
                ("description", models.TextField()),
            ],
            options={
                "ordering": ("name",),
            },
        ),
        migrations.AlterField(
            model_name="conference",
            name="abstract_deadline",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(2017, 5, 24, 2, 25, 26, 918734, tzinfo=utc),
                verbose_name="Deadline of Abstract Submission",
            ),
        ),
        migrations.AlterField(
            model_name="conference",
            name="end_date",
            field=models.DateField(
                default=datetime.datetime(2017, 6, 10, 2, 25, 26, 918734, tzinfo=utc),
                verbose_name="Date Ended",
            ),
        ),
        migrations.AlterField(
            model_name="conference",
            name="paper_deadline",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(2017, 5, 29, 2, 25, 26, 918734, tzinfo=utc),
                verbose_name="Deadline of Paper Submission",
            ),
        ),
        migrations.AlterField(
            model_name="conference",
            name="start_date",
            field=models.DateField(
                default=datetime.datetime(2017, 6, 8, 2, 25, 26, 918734, tzinfo=utc),
                verbose_name="Date Started",
            ),
        ),
    ]

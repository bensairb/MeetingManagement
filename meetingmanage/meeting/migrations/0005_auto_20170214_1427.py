# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0004_auto_20170214_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='activity_time',
        ),
        migrations.AlterField(
            model_name='activity',
            name='end_time',
            field=models.TimeField(verbose_name='end time'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start_time',
            field=models.TimeField(verbose_name='start time'),
        ),
    ]

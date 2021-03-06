# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 00:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name of activity')),
                ('position', models.CharField(max_length=200, verbose_name='position of activity')),
                ('start_time', models.DateTimeField(verbose_name='start time')),
                ('end_time', models.DateTimeField(verbose_name='end time')),
                ('activity_code', models.CharField(editable=False, max_length=200)),
            ],
        ),
    ]

from datetime import *
import random

from django.db import models

class Activity(models.Model):
    activity_name = models.CharField('name of activity',max_length=200)
    activity_position = models.CharField('position of activity',max_length=200)
    activity_day = models.DateField('activity day')
    start_time = models.TimeField('start time')
    end_time = models.TimeField('end time')


    def __str__(self):
        return '%s' % (self.activity_name)

    def get_activity_time(self):
        start_hour = self.start_time.strftime('%H:%M')
        end_hour = self.end_time.strftime('%H:%M')
        return start_hour + '-' + end_hour

    get_activity_time.short_description = 'time'

    def get_activity_day(self):
        return self.activity_day.strftime('%Y-%m-%d')

    def was_ended(self):
        return self.activity_day < date.today()

    def _create_activity_code(self):
        ch=['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        strlist = random.sample(ch,5)
        randomstr = ''
        return randomstr.join(strlist)

    activity_code = property(_create_activity_code)
    get_activity_day.short_description = 'date'
    was_ended.boolean = True

from django.db import models

class Activity(models.Model):
    name = models.CharField('name of activity',max_length=200)
    position = models.CharField('position of activity',max_length=200)
    start_time = models.DateTimeField('start time')
    end_time = models.DateTimeField('end time')
    activity_code = models.CharField(max_length=200,editable=False)

    def __str__(self):
        return '%s' % (self.name)

    def get_time_segment(self):
        time_segment = self.end_time - self.end_time
        return time_segment

    def create_activity_code(self):
        pass

from django.contrib import admin
from .models import Activity

# Register your models here.
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        'activity_name',
        'activity_position',
        'get_activity_day',
        'get_activity_time',
        'was_ended',
        'activity_code'
    )

admin.site.register(Activity,ActivityAdmin)
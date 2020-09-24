from django.contrib import admin
from .models import User, UserProfileInfo,teacher_timetable

# Register your models here.

class UserProfileInfoAdmin(admin.ModelAdmin):

    fields=['rollnumber','specialization','class_Group']

    search_fields=['rollnumber','specialization']

    list_filter=['specialization'.lower()]

    #list_display=['rollnumber','specialization']



admin.site.register(UserProfileInfo,UserProfileInfoAdmin)
admin.site.register(teacher_timetable)

from .models import student_tymtable
admin.site.register(student_tymtable)

from .models import teacher_name
admin.site.register(teacher_name)

from django.contrib import admin
from .models import User, UserProfileInfo

# Register your models here.

class UserProfileInfoAdmin(admin.ModelAdmin):

    fields=['rollnumber','specialization']

    search_fields=['rollnumber','specialization']

    list_filter=['specialization'.lower()]

    #list_display=['rollnumber','specialization']



admin.site.register(UserProfileInfo,UserProfileInfoAdmin)
# admin.site.register(UserProfileInfoForm)

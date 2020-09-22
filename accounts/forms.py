from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo,teacher_timetable

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    specialization = forms.CharField(max_length=10)
    rollnumber = forms.CharField(max_length=10) #danger charfield
    class_Group=forms.CharField(max_length=10)
    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('specialization','rollnumber','class_Group')


class teacher_timetableform(forms.ModelForm):
    class Meta():
        model=teacher_timetable
        fields='__all__'

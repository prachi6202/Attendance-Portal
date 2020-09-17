from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model
Days = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)

Group=(
    ('1','1'),
    ('2','2'),
    ('3','3'),
)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=10)
    rollnumber = models.CharField(max_length=10)
    class_grp=models.CharField(max_length=10,choices=Group,default='1')

    def __str__(self):
        return self.user.username

class student_tymtable(models.Model):
    class_grp = models.CharField(max_length=10, choices=Group, default='1')
    specialization=models.CharField(max_length=10,default="")
    day=models.CharField(max_length=50, choices=Days, default='Monday')
    First_lech=models.CharField(max_length=50, null=True,blank=True)
    sec_lech=models.CharField(max_length=50, null=True,blank=True)
    third_lech=models.CharField(max_length=50, null=True,blank=True)
    fourth_lech=models.CharField(max_length=50, null=True,blank=True)
    fifth_lech=models.CharField(max_length=50, null=True,blank=True)
    sixth_lech=models.CharField(max_length=50, null=True,blank=True)
    sev_lech=models.CharField(max_length=50, null=True,blank=True)
    First_lech_teacher = models.CharField(max_length=50, null=True,blank=True)
    sec_lech_teacher = models.CharField(max_length=50, null=True,blank=True)
    third_lech_teacher = models.CharField(max_length=50, null=True,blank=True)
    fourth_lech_teacher = models.CharField(max_length=50, null=True,blank=True)
    fifth_lech_teacher = models.CharField(max_length=50, null=True,blank=True)
    sixth_lech_teacher = models.CharField(max_length=50, null=True,blank=True)
    sev_lech_teacher = models.CharField(max_length=50, null=True,blank=True)

    def __str__(self):
        return '{} {}'.format(str(self.specialization),str(self.day),str(self.First_lech_teacher),
                              str(self.sec_lech_teacher),str(self.third_lech_teacher),str(self.fourth_lech_teacher),
                              str(self.fifth_lech_teacher),str(self.sixth_lech_teacher),str(self.sev_lech_teacher))




class teacher_timetable(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=70)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default='1')
    day=models.CharField(max_length=50, choices=Days, default='Monday')
    First_lech=models.CharField(max_length=50, null=True,blank=True)
    sec_lech=models.CharField(max_length=50, null=True,blank=True)
    third_lech=models.CharField(max_length=50, null=True,blank=True)
    fourth_lech=models.CharField(max_length=50, null=True,blank=True)
    fifth_lech=models.CharField(max_length=50, null=True,blank=True)
    sixth_lech=models.CharField(max_length=50, null=True,blank=True)
    sev_lech=models.CharField(max_length=50, null=True,blank=True)
    First_link=models.CharField(max_length=50, null=True,blank=True)
    sec_link=models.CharField(max_length=50, null=True,blank=True)
    third_link=models.CharField(max_length=50, null=True,blank=True)
    fourth_link=models.CharField(max_length=50, null=True,blank=True)
    fifth_link=models.CharField(max_length=50, null=True,blank=True)
    sixth_link=models.CharField(max_length=50, null=True,blank=True)
    sev_link=models.CharField(max_length=50, null=True,blank=True)

    def __str__(self):
        return '{} {}'.format(str(self.name),str(self.day))


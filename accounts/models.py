from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=10)
    rollnumber = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username

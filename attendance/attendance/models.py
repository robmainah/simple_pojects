from django.db import models
from django.contrib.auth.models import User

from user.models import Profile

class Subject(models.Model):
    title = models.CharField(max_length=255, unique=True)


class Attendance(models.Model):
    student = models.OneToOneField(Profile, related_name='attendances', on_delete=models.CASCADE)
    subject = models.OneToOneField(Subject, related_name='attendances', on_delete=models.CASCADE)
    teacher = models.OneToOneField(User, related_name='attendances', on_delete=models.CASCADE)
    attendance_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

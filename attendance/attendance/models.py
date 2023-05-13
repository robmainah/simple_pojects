from django.db import models
from django.contrib.auth.models import User

from user.models import Profile


class StudentClass(models.Model):
    title = models.CharField(max_length=255, unique=True)
    
    def __str__(self) -> str:
        return f'{self.title}'

class Subject(models.Model):
    title = models.CharField(max_length=255, unique=True)
    teacher = models.ForeignKey(User, related_name='subjects', on_delete=models.CASCADE)
    student_class = models.ForeignKey(StudentClass, related_name='subjects', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.title}'


class Attendance(models.Model):
    student = models.ForeignKey(Profile, related_name='attendances', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='attendances', on_delete=models.CASCADE)
    date_attended = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.student.user.first_name} {self.subject} attendance'

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    registration_no = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name} profile'

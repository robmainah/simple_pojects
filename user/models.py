from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    registration_no = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.name

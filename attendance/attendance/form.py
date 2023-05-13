from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import Subject
   

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

    # def save(self):
    #     instance = super().save(commit=False)
    #     instance.password = make_password(get_random_string(length=6))
    #     instance.username = self.cleaned_data.get('email')
    #     instance.is_staff = True
        
    #     return super().save()


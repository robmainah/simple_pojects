from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.ModelForm):
    password = forms.CharField()
    email = forms.CharField()
    class Meta:
        model = Profile
        fields = ['email', 'password']
    

class AddTeacherForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def save(self):
        instance = super().save(commit=False)
        instance.password = make_password(get_random_string(length=6))
        instance.username = self.cleaned_data.get('email')
        instance.is_staff = True
        
        return super().save()
    

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()
    confirm_password = forms.CharField()

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'registration_no', 'email', 'phone', 'password', 'confirm_password']

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        instance = self.instance

        qs = User.objects.filter(email__iexact=email)

        if instance is not None:
            qs = qs.exclude(pk=instance.pk)

        if qs.exists():
            raise forms.ValidationError('Email is already used')
        
        return email
        
    def clean_confirm_password(self, *args, **kwargs):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')

        return confirm_password
    
    def save(self, user):
        instance = super().save(commit=False)
        instance.user = user
        return super().save()
    
class LoginForm(forms.ModelForm):
    password = forms.CharField()
    email = forms.CharField()
    class Meta:
        model = Profile
        fields = ['email', 'password']
    

class AddStudentForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'registration_no', 'email', 'phone']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        instance = self.instance

        qs = User.objects.filter(email__iexact=email)

        if instance is not None:
            qs = qs.exclude(pk=instance.pk)

        if qs.exists():
            raise forms.ValidationError('Email is already used')
        
        return email    
    
    def save(self, user):
        instance = super().save(commit=False)
        instance.user = user
        return super().save()

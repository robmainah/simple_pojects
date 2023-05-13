from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

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

        if qs.exists() and email != instance.user.email:
            raise forms.ValidationError('Email is already used')
        
        return email    
    
    def save(self, user):
        instance = super().save(commit=False)
        instance.user = user
        return super().save()

from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import Subject, Attendance, StudentClass
   

class StudentClassForm(forms.ModelForm):
    class Meta:
        model = StudentClass
        fields = '__all__'

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'
        widgets = {
            'date_attended': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd'}
            )
        }

    # def save(self):
    #     instance = super().save(commit=False)
    #     instance.password = make_password(get_random_string(length=6))
    #     instance.username = self.cleaned_data.get('email')
    #     instance.is_staff = True
        
    #     return super().save()


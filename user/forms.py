from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import Student

class ProfileRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField()

    class Meta:
        model = Student
        fields = ['name', 'registration_no', 'email', 'phone', 'password', 'confirm_password']

    def clean_confirm_password(self, *args, **kwargs):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')

        return confirm_password
    

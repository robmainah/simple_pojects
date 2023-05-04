from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import Profile
from .forms import RegistrationForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            data = {
                'username': form.cleaned_data.get('email'),
                'email': form.cleaned_data.get('email'),
                'first_name': form.cleaned_data.get('first_name'),
                'last_name': form.cleaned_data.get('last_name'),
                'is_staff': False,
            }

            user = User.objects.create(**data)
            form.save(user)

            messages.success(request, 'Registration successful')
            return redirect('user-register')    
    else:
        form = RegistrationForm()

    return render(request, 'user/register.html', { 'form': form })

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():

            messages.success(request, 'Login successful')
            return redirect('login')    
    else:
        form = LoginForm()

    return render(request, 'user/login.html', { 'form': form })

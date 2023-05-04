from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password

from .models import Profile
from .forms import RegistrationForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            # print(make_password(form.cleaned_data.get('password')))
            data = {
                'username': form.cleaned_data.get('email'),
                'email': form.cleaned_data.get('email'),
                'first_name': form.cleaned_data.get('first_name'),
                'last_name': form.cleaned_data.get('last_name'),
                'password': make_password(form.cleaned_data.get('password')),
                'is_staff': False,
            }

            user = User.objects.create(**data)
            form.save(user)

            messages.success(request, 'Registration successful')
            return redirect('login')    
    else:
        form = RegistrationForm()

    return render(request, 'user/register.html', { 'form': form })

def profile_login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user/login.html', { 'form': form })

    form = LoginForm(request.POST)

    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('reservations-index')
        else:
            messages.warning(request, 'Wrong credintials')
            return redirect('login')
 

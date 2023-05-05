from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.crypto import get_random_string

from .forms import RegistrationForm, LoginForm, AddStudentForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
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
            return redirect('reservations')
        else:
            messages.warning(request, 'Wrong credintials')
            return redirect('login')
 

def students(request):
    students_list = User.objects.filter(is_staff=False).order_by('-date_joined')

    page = request.GET.get('page', 1)
    paginator = Paginator(students_list, 10)

    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    return render(request, 'user/all_students.html', { 'students': students })


def add_student(request):
    if request.method == 'GET':
        form = AddStudentForm()

        return render(request, 'user/add_student.html', { 'form': form })
    else:
        form = AddStudentForm(request.POST)

        if form.is_valid():
            form.cleaned_data['password'] = get_random_string(length=6)

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
            form = AddStudentForm()

            messages.success(request, 'Student created successfully')
            return redirect('students')

        return render(request, 'user/add_student.html', { 'form': form })

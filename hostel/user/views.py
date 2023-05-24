from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm, LoginForm, AddStudentForm

from .models import Profile

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
        if request.user is not None and request.user == 'AnonymousUser':
            return redirect('reservations')

        form = RegistrationForm()

    return render(request, 'user/register.html', { 'form': form })

def student_login(request):
    if request.method == 'GET':
        if request.user is not None and request.user == 'AnonymousUser':
            return redirect('reservations')
        
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
 
@login_required
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

@login_required
def add_student(request):
    if request.method == 'GET':
        form = AddStudentForm()

        return render(request, 'user/student_form.html', { 'form': form })
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

        return render(request, 'user/student_form.html', { 'form': form })

@login_required
def edit_student(request, pk):
    student = get_object_or_404(Profile, pk=pk)

    if request.method == 'GET':
        form = AddStudentForm(instance=student)
        form.fields['first_name'].initial = student.user.first_name
        form.fields['last_name'].initial = student.user.last_name
        form.fields['email'].initial = student.user.email

        return render(request, 'user/student_form.html', { 'form': form, 'id' : student.id })
    else:
        form = AddStudentForm(request.POST, instance=student)            

        if form.is_valid():
            data = {
                'username': form.cleaned_data.get('email'),
                'email': form.cleaned_data.get('email'),
                'first_name': form.cleaned_data.get('first_name'),
                'last_name': form.cleaned_data.get('last_name'),
            }

            user = User.objects.filter(pk=student.user.pk)
            user.update(**data)

            form.save(user.first())
            form = AddStudentForm()

            return redirect('students')

        return render(request, 'user/student_form.html', { 'form': form, 'id' : student.id })


@login_required
def delete_student(request, pk):
    student = get_object_or_404(Profile, pk=pk)
    student.user.delete()

    return redirect('students')

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, AddStudentForm
from .teacherForm import AddTeacherForm

from .models import Profile

def student_login(request):
    if request.method == 'GET':
        print(request.user)
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
def teachers(request):
    teachers_list = User.objects.filter(is_staff=True, is_superuser=False).order_by('-date_joined')

    page = request.GET.get('page', 1)
    paginator = Paginator(teachers_list, 10)

    try:
        teachers = paginator.page(page)
    except PageNotAnInteger:
        teachers = paginator.page(1)
    except EmptyPage:
        teachers = paginator.page(paginator.num_pages)

    return render(request, 'user/all_teachers.html', { 'teachers': teachers })

@login_required
def add_teacher(request):
    if request.method == 'GET':
        form = AddTeacherForm()

        return render(request, 'user/teacher_form.html', { 'form': form })
    else:
        form = AddTeacherForm(request.POST)

        if form.is_valid():
            form.save()
            form = AddTeacherForm()

            return redirect('teachers')

        return render(request, 'user/teacher_form.html', { 'form': form })

@login_required
def edit_teacher(request, pk):
    teacher = get_object_or_404(User, pk=pk)

    if request.method == 'GET':
        form = AddTeacherForm(instance=teacher)

        return render(request, 'user/teacher_form.html', { 'form': form, 'id' : teacher.id })
    else:
        form = AddTeacherForm(request.POST, instance=teacher)            

        if form.is_valid():
            form.save()
            form = AddTeacherForm()

            return redirect('teachers')

        return render(request, 'user/teacher_form.html', { 'form': form, 'id' : teacher.id })


@login_required
def delete_student(request, pk):
    student = get_object_or_404(Profile, pk=pk)
    student.user.delete()

    return redirect('students')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from .form import StudentClassForm

from .models import StudentClass

@login_required
def student_classes(request):
    student_class_list = StudentClass.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(student_class_list, 10)

    try:
        student_class = paginator.page(page)
    except PageNotAnInteger:
        student_class = paginator.page(1)
    except EmptyPage:
        student_class = paginator.page(paginator.num_pages)

    return render(request, 'attendances/student_classes.html', { 'student_class': student_class })

@login_required
def add_student_class(request):
    if request.method == 'GET':
        form = StudentClassForm()

        return render(request, 'attendances/student_class_form.html', { 'form': form })
    else:
        form = StudentClassForm(request.POST)

        if form.is_valid():
            form.save()
            form = StudentClassForm()

            return redirect('student_classes')

        return render(request, 'attendances/student_class_form.html', { 'form': form })

@login_required
def edit_student_class(request, pk):
    student_class = get_object_or_404(StudentClass, pk=pk)

    if request.method == 'GET':
        form = StudentClassForm(instance=student_class)

        return render(request, 'attendances/student_class_form.html', { 'form': form, 'id' : student_class.id })
    else:
        form = StudentClassForm(request.POST, instance=student_class)            

        if form.is_valid():
            form.save()
            form = StudentClassForm()

            return redirect('student_classes')

        return render(request, 'attendances/student_class_form.html', { 'form': form, 'id' : student_class.id })


@login_required
def delete_student_class(request, pk):
    student_class = get_object_or_404(StudentClass, pk=pk)
    student_class.delete()

    return redirect('student_classes')

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from .form import AttendanceForm

from .models import Attendance

@login_required
def attendances(request):
    attendances_list = Attendance.objects.filter()

    page = request.GET.get('page', 1)
    paginator = Paginator(attendances_list, 10)

    try:
        attendances = paginator.page(page)
    except PageNotAnInteger:
        attendances = paginator.page(1)
    except EmptyPage:
        attendances = paginator.page(paginator.num_pages)

    return render(request, 'attendances/attendances.html', { 'attendances': attendances })

@login_required
def add_attendance(request):
    if request.method == 'GET':
        form = AttendanceForm()

        return render(request, 'attendances/attendance_form.html', { 'form': form })
    else:
        form = AttendanceForm(request.POST)

        if form.is_valid():
            form.save()
            form = AttendanceForm()

            return redirect('attendances')

        return render(request, 'attendances/attendance_form.html', { 'form': form })

@login_required
def edit_attendance(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)

    if request.method == 'GET':
        form = AttendanceForm(instance=attendance)

        return render(request, 'attendances/attendance_form.html', { 'form': form, 'id' : attendance.id })
    else:
        form = AttendanceForm(request.POST, instance=attendance)            

        if form.is_valid():
            form.save()
            form = AttendanceForm()

            return redirect('attendances')

        return render(request, 'attendances/attendance_form.html', { 'form': form, 'id' : attendance.id })


@login_required
def delete_attendance(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    attendance.delete()

    return redirect('attendances')

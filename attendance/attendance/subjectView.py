from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from .form import SubjectForm

from .models import Subject

@login_required
def subjects(request):
    subjects_list = Subject.objects.filter()

    page = request.GET.get('page', 1)
    paginator = Paginator(subjects_list, 10)

    try:
        subjects = paginator.page(page)
    except PageNotAnInteger:
        subjects = paginator.page(1)
    except EmptyPage:
        subjects = paginator.page(paginator.num_pages)

    return render(request, 'attendances/subjects.html', { 'subjects': subjects })

@login_required
def add_subject(request):
    if request.method == 'GET':
        form = SubjectForm()
        form.fields['teacher'].queryset = User.objects.filter(is_staff=True, is_superuser=False)

        return render(request, 'attendances/subject_form.html', { 'form': form })
    else:
        form = SubjectForm(request.POST)

        if form.is_valid():
            form.save()
            form = SubjectForm()

            return redirect('subjects')

        return render(request, 'attendances/subject_form.html', { 'form': form })

@login_required
def edit_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)

    if request.method == 'GET':
        form = SubjectForm(instance=subject)

        return render(request, 'attendances/subject_form.html', { 'form': form, 'id' : subject.id })
    else:
        form = SubjectForm(request.POST, instance=subject)            

        if form.is_valid():
            form.save()
            form = SubjectForm()

            return redirect('subjects')

        return render(request, 'attendances/subject_form.html', { 'form': form, 'id' : subject.id })


@login_required
def delete_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()

    return redirect('subjects')

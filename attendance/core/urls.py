"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from user import teacherView
from attendance import subjectView, studentClassView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),

    path('teachers/', teacherView.teachers, name='teachers'),
    path('teachers/add_teacher/', teacherView.add_teacher, name='add_teacher'),
    path('teachers/edit/<int:pk>/', teacherView.edit_teacher, name='edit_teacher'),
    path('teachers/delete/<int:pk>/', teacherView.delete_teacher, name='delete_teacher'),

    path('subjects/', subjectView.subjects, name='subjects'),
    path('subjects/add_subject/', subjectView.add_subject, name='add_subject'),
    path('subjects/edit/<int:pk>/', subjectView.edit_subject, name='edit_subject'),
    path('subjects/delete/<int:pk>/', subjectView.delete_subject, name='delete_subject'),

    path('student_classes/', studentClassView.student_classes, name='student_classes'),
    path('student_classes/add/', studentClassView.add_student_class, name='add_student_class'),
    path('student_classes/edit/<int:pk>/', studentClassView.edit_student_class, name='edit_student_class'),
    path('student_classes/delete/<int:pk>/', studentClassView.delete_student_class, name='delete_student_class'),
    
    path('attendances/', include('attendance.urls'), name='main'),
    path('', RedirectView.as_view(url='attendances'), name='home'),
]

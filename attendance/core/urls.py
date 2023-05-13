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

from reservation import views
from user.views import student_login
from user import teacherView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),
    path('reservations/', include('reservation.urls')),
    path('payments/', views.payments, name='payments'),

    path('teachers/', teacherView.teachers, name='teachers'),
    path('teachers/add_teacher/', teacherView.add_teacher, name='add_teacher'),
    path('teachers/edit/<int:pk>/', teacherView.edit_teacher, name='edit_teacher'),
    
    path('payments/new/', views.add_payment, name='add_payment'),
    path('payments/edit/<int:pk>/', views.edit_payment, name='edit_payment'),
    path('payments/delete/<int:pk>/', views.delete_payment, name='delete_payment'),
    path('', views.all_reservations, name='main'),
]

from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login/', views.student_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('students/', views.students, name='students'),
    path('students/add_student/', views.add_student, name='add_student'),
    path('students/edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:pk>/', views.delete_student, name='delete_student'),
]

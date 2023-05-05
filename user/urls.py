from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.profile_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('students/', views.students, name='students'),
    path('add_student/', views.add_student, name='add_student'),
]

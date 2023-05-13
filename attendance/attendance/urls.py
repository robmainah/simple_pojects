from django.urls import path

from . import views

urlpatterns = [
    path('', views.attendances, name='attendances'),
    path('add/', views.add_attendance, name='add_attendance'),
    path('edit/<int:pk>/', views.edit_attendance, name='edit_attendance'),
    path('delete/<int:pk>/', views.delete_attendance, name='delete_attendance'),
]

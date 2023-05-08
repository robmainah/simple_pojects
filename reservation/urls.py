from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='reservations'),
    path('new/', views.add_reservation, name='add_reservation'),
    path('edit/<int:pk>/', views.edit_reservation, name='edit_reservation'),
    path('delete/<int:pk>/', views.delete_reservation, name='delete_reservation'),
]

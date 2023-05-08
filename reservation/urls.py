from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='reservations'),
    path('new/', views.add_reservation, name='add_reservation'),
    path('new/', views.add_payment, name='add_payment'),
]

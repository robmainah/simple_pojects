from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_rooms, name='rooms'),
    path('new/', views.add_room, name='add_room'),
    path('edit/<int:pk>/', views.edit_room, name='edit_room'),
    path('delete/<int:pk>/', views.delete_room, name='delete_room'),
]
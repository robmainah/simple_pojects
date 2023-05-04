from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    room_no = models.IntegerField(unique=True)
    has_empty = models.BooleanField(default=True)
    amount = models.FloatField(default=0)

    def __str__(self) -> str:
        return str(self.room_no)
    

class Reservation(models.Model):
    user = models.ForeignKey(User, related_name='reservations', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='reservations', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='updated_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.room} - {self.user}'

class Payment(models.Model):
    reservation = models.ForeignKey(Reservation, related_name='payments', on_delete=models.CASCADE, null=True)
    # room = models.ForeignKey(Room, related_name='payments', on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    balance = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.reservation}'

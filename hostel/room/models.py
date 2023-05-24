from django.db import models

class Room(models.Model):
    room_no = models.IntegerField(unique=True)
    has_empty = models.BooleanField(default=True)
    amount = models.FloatField(default=0)

    def __str__(self) -> str:
        return str(self.room_no)

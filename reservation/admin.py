from django.contrib import admin

from .models import Reservation, Room, Payment

admin.site.register(Reservation)
admin.site.register(Room)
admin.site.register(Payment)

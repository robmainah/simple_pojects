from django.shortcuts import render

from .models import Reservation

def index(request):
    if request.user.is_staff:
        reservations = Reservation.objects.all()
    else:
        reservations = Reservation.objects.filter(user=request.user)

    print(reservations)


    return render(request, 'reservations/index.html', { 'reservations': reservations })

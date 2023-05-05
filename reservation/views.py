from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Reservation, Room
from .forms import AddReservationForm

def index(request):
    if request.user.is_staff:
        reservations_list = Reservation.objects.all().order_by('-created_at')
    else:
        reservations_list = Reservation.objects.filter(user=request.user).order_by('-created_at')

    paginator = Paginator(reservations_list, 2)
    page = request.GET.get('page', 1)

    try:
        reservations = paginator.page(page)
    except PageNotAnInteger:
        reservations = paginator.page(1)
    except EmptyPage:
        reservations = paginator.page(paginator.num_pages)

    return render(request, 'reservations/index.html', { 'reservations': reservations })


def add_reservation(request):
    rooms = Room.objects.all()
    students = User.objects.filter(is_staff=False)

    context = {
        'rooms': rooms,
        'students': students,
    }

    if request.method == 'POST':
        form = AddReservationForm(request.POST)

        if form.is_valid():
            form.save(request.user)
            return redirect('reservations')
        else:
            messages.warning(request, 'Please fill all fields')

            context['form'] = request.POST

            return render(request, 'reservations/form.html', { 'context': context })

    else:
        context['form'] = {
            'user': 0,
            'room': '',
            'is_active': '',
        }

        return render(request, 'reservations/form.html', { 'context': context })

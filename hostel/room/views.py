from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from .models import Room
from .forms import AddRoomForm

@login_required
def all_rooms(request):
    rooms_list = Room.objects.all()

    paginator = Paginator(rooms_list, 5)
    page = request.GET.get('page', 1)

    try:
        rooms = paginator.page(page)
    except PageNotAnInteger:
        rooms = paginator.page(1)
    except EmptyPage:
        rooms = paginator.page(paginator.num_pages)

    return render(request, 'rooms/index.html', { 'rooms': rooms })

@login_required
def add_room(request):
    if request.method == 'POST':
        form = AddRoomForm(request.POST)

        if form.is_valid():
            form.save(request.user)
            return redirect('rooms')
        else:
            messages.warning(request, 'Please fill all fields')
            return render(request, 'rooms/room_form.html', { 'form': form })
    else:
        form = AddRoomForm()
        return render(request, 'rooms/room_form.html', { 'form': form })

@login_required
def edit_room(request, pk):
    room = get_object_or_404(Room, pk=pk)

    if request.method == 'POST':
        form = AddRoomForm(request.POST, instance=room)

        if form.is_valid():
            form.save()
            return redirect('rooms')
        else:
            messages.warning(request, 'Please fill all fields')
            
            return render(request, 'rooms/room_form.html', { 'form': form, 'id': room.pk })
    else:
        form = AddRoomForm(instance=room)
        return render(request, 'rooms/room_form.html', { 'form': form, 'id': room.pk })


@login_required
def delete_room(request, pk):
    get_object_or_404(Room, pk=pk).delete()
    return redirect('rooms')


@login_required
def payments(request):
    if request.user.is_staff:
        payments_list = Payment.objects.all().order_by('-created_at')
    else:
        payments_list = Payment.objects.filter(room__user=request.user).order_by('-created_at')

    paginator = Paginator(payments_list, 10)
    page = request.GET.get('page', 1)

    try:
        payments = paginator.page(page)
    except PageNotAnInteger:
        payments = paginator.page(1)
    except EmptyPage:
        payments = paginator.page(paginator.num_pages)

    return render(request, 'rooms/payments.html', { 'payments': payments })

@login_required
def add_payment(request):
    if request.method == 'GET':
        form = AddPaymentForm()

        form.fields['room'].queryset = Room.objects.filter(user = request.user)

        return render(request, 'rooms/payment_form.html', { 'form' : form })    
    
    form = AddPaymentForm(request.POST)

    if form.is_valid():
        form.save()
        form = AddPaymentForm()
        return redirect('payments')

    return render(request, 'rooms/payment_form.html', { 'form' : form })

@login_required
def edit_payment(request, pk):
    payment = get_object_or_404(Payment, pk=pk)

    if request.method == 'GET':
        form = AddPaymentForm(instance=payment)
        return render(request, 'rooms/payment_form.html', { 'form' : form, 'id' : payment.pk })    
    
    form = AddPaymentForm(request.POST, instance=payment)

    if form.is_valid():
        form.save()
        form = AddPaymentForm()
        return redirect('payments')

    return render(request, 'rooms/payment_form.html', { 'form' : form })

@login_required
def delete_payment(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    payment.delete()

    return redirect('payments')

from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .models import Student
from .forms import ProfileRegistrationForm

def register(request):
    if request.method == 'POST':
        form = ProfileRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful')
            return redirect('user-register')    
    else:
        form = ProfileRegistrationForm()

    return render(request, 'user/register.html', { 'form': form })

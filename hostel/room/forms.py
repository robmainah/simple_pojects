from django import forms

from .models import Room

class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_no', 'has_empty', 'amount']
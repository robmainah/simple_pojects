from django import forms

from .models import Reservation, Payment

class AddReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['user', 'room', 'is_active']

    def save(self, user):
        instance = super().save(commit=False)
        instance.created_by = user
        instance.updated_by = user

        return super().save()


class AddPaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['reservation', 'amount', 'balance']

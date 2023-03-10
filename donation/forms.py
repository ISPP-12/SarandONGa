from django.utils import timezone
from django import forms

class CreateNewDonation(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(required=False)
    created_date = forms.DateTimeField(initial=timezone.now, required=False)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    donor_name = forms.CharField(max_length=100)
    donor_surname = forms.CharField(max_length=250)
    donor_dni = forms.CharField(max_length=9)
    donor_address = forms.CharField(max_length=200)
    donor_email = forms.EmailField()
    
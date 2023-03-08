from django.shortcuts import render
from .forms import create_payment_form
from .models import Payment
from django.contrib import messages

def create_payment(request):
    if request.method == 'POST':
        form = create_payment_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, 'El formulario presenta errores')
    else:
        form = create_payment_form()
    return render(request, 'payment/create_donation.html', {'form': form})

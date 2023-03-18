from django.shortcuts import render, get_object_or_404, redirect
from .forms import create_payment_form
from .models import Payment
from django.contrib import messages
# import json


def payment_create(request):
    if request.method == 'POST':
        form = create_payment_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, 'El formulario presenta errores')
    else:
        form = create_payment_form()
    return render(request, 'payment/payment_form_malo.html', {'form': form})


def payment_update(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    form = create_payment_form(instance=payment)

    if request.method == 'POST':
        form = create_payment_form(
            request.POST, request.FILES, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('/payment/list')

    context = {'form': form}
    return render(request, 'payment/payment_form_malo.html', context)


def payment_list(request):
    context = {
        'objects': Payment.objects.all(),
        # 'objects_json': json.dumps(list(Payment.objects.all().values())),
        'objects_name': 'Payment',
        'title': 'Lista de Pagos'
    }

    return render(request, 'payment/payment_list.html', context)

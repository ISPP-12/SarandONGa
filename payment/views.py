from django.shortcuts import render, get_object_or_404, redirect
from .forms import CreatePaymentForm
from .models import Payment
from django.contrib import messages
import json
from django.contrib.auth.decorators import login_required
from main.views import custom_403

@login_required
def payment_create(request):
    form = CreatePaymentForm(initial={'ong': request.user.ong})
    if request.method == 'POST':
        form = CreatePaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.ong = request.user.ong
            payment.save()
            return redirect('payment_list')

        else:
            messages.error(request, 'El formulario presenta errores')
    else:
        form = CreatePaymentForm()

        events = [
        {
        "title": '100 €',
        "start": '2023-03-01',
        "end": '2023-03-01',
        "extendedProps": {
            "type": 'payment',
            "id": 1,
            "amount": 100,
            "observations": 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quod.',
            "paid": True,
        },
        },
        {
        "title": '10 €',
        "start": '2023-03-01',
        "end": '2023-03-01',
        "extendedProps": {
            "type": 'payment',
            "id": 10,
            "amount": 100,
            "observations": 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quod.',
            "paid": False,
        },
        },
        {
        "title": 'Fisioterapia',
        "start": '2023-03-04',
        "end": '2023-03-012',
        "extendedProps": {
            "type": 'service',
            "id": 10,
            "amount": 100,
            "observations": 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quod.',
            "paid": False,
        },
        },
        {
        "title": 'Fisioterapia',
        "start": '2023-03-08',
        "end": '2023-03-08'
        },
        {
        "title": '100€',
        "start": '2023-03-09',
        "end": '2023-03-09'
        },
        {
        "title": '100€',
        "start": '2023-03-10',
        "end": '2023-03-10'
        },
        {
        "title": 'Trabajo Social',
        "start": '2023-03-11',
        "end": '2023-03-11'
        },
    ]
        events_json= json.dumps(events)

    return render(request, 'payment/payment_form.html', {'form': form, 'title': 'Añadir Pago', 'events_json':events_json})

@login_required
def payment_update(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    form = CreatePaymentForm(instance=payment)
    if request.user.ong == payment.ong:
        if request.method == 'POST':
            form = CreatePaymentForm(
                request.POST, request.FILES, instance=payment)
            if form.is_valid():
                form.save()
                return redirect('/payment/list')

        context = {'form': form, 'title': 'Actualizar pago'}
    else:
        return custom_403(request)
    return render(request, 'payment/payment_form.html', context)

@login_required
def payment_list(request):
    context = {
        'objects': Payment.objects.filter(ong=request.user.ong).values(),
        # 'objects_json': json.dumps(list(Payment.objects.all().values())),
        'objects_name': 'Payment',
        'title': 'Lista de Pagos'
    }

    return render(request, 'payment/payment_list.html', context)

@login_required
def payment_delete(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    if request.user.ong == payment.ong:
        payment.delete()
    else:
        return custom_403(request)
    return redirect('payment_list')

@login_required
def payment_details(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    if request.user.ong == payment.ong:
        return render(request, 'payment/payment_details.html', {'payment': payment})
    else:
        return custom_403(request)
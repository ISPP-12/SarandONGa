from django.shortcuts import render, get_object_or_404, redirect
from .forms import CreatePaymentForm
from .models import Payment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.views import custom_403
# import json

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

    return render(request, 'payment/payment_form.html', {'form': form, 'title': 'Añadir Pago'})

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
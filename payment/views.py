from django.shortcuts import render, get_object_or_404, redirect
from .forms import CreatePaymentForm
from .models import Payment
from django.contrib import messages
import json
from django.contrib.auth.decorators import login_required
from main.views import custom_403
from datetime import datetime


# Hay que asignar el padrino
@login_required
def payment_create(request):
    form = CreatePaymentForm(initial={'ong': request.user.ong})
    if request.method == 'POST':
        form = CreatePaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.ong = request.user.ong
            payment.save()
            return redirect('payment_create')

        else:
            messages.error(request, 'El formulario presenta errores')
    else:

        all_events = Payment.objects.all()
        event_arr = []
        for i in all_events:
            event_sub_arr = {}
            event_sub_arr['title'] = "{} - {}".format(i.concept, i.amount)
            # start_date = datetime.strptime(str(i.payday.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            # end_date = datetime.strptime(str(i.payday.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            start_date = i.payday
            end_date = i.payday
            event_sub_arr['start'] = start_date
            event_sub_arr['end'] = end_date
            event_sub_arr['url'] = "./"+str(i.id)+"/update"
            event_sub_arr['id'] = str(i.id)
            event_arr.append(event_sub_arr)
        datatest = json.dumps(event_arr, default=str)

    context = {'form': form, 'title': 'Añadir pago', 'events_json': datatest}

    return render(request, 'payment/payment_form.html', context)


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
                return redirect('/payment/create')
        else:
            all_events = Payment.objects.all()
            event_arr = []
            for i in all_events:
                event_sub_arr = {}
                event_sub_arr['title'] = "{} - {}".format(i.concept, i.amount)
                start_date = i.payday
                end_date = i.payday
                event_sub_arr['start'] = start_date
                event_sub_arr['end'] = end_date
                event_sub_arr['id'] = str(i.id)
                event_arr.append(event_sub_arr)
            datatest = json.dumps(event_arr, default=str)

        context = {'form': form, 'title': 'Actualizar pago',
                   'events_json': datatest}
    else:
        return custom_403(request)
    return render(request, 'payment/payment_form.html', context)


@login_required
def payment_list(request):
    context = {
        'objects': Payment.objects.filter(ong=request.user.ong).values(),
        # 'objects_json': json.dumps(list(Payment.objects.all().values())),
        'objects_name': 'Payment',
        'title': 'Gestión de Pagos'
    }

    return render(request, 'payment/payment_list.html', context)


@login_required
def payment_delete(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    if request.user.ong == payment.ong:
        payment.delete()
    else:
        return custom_403(request)
    return redirect('/payment/create')


@login_required
def payment_details(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    if request.user.ong == payment.ong:
        return render(request, 'payment/payment_details.html', {'payment': payment})
    else:
        return custom_403(request)

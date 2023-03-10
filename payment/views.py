from django.shortcuts import render
from .models import Payment
#import json

def payment_list(request):
    context = {
        'objects': Payment.objects.all(),
        #'objects_json': json.dumps(list(Payment.objects.all().values())),
        'objects_name': 'Payment',
        'title': 'Lista de Pagos'
    }
    return render(request, 'payment/payment_list.html', {"context":context })
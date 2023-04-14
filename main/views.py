import json
from django.shortcuts import render, redirect
from functools import wraps
from django.contrib import messages
from person.models import ASEMUser, Worker, Volunteer, GodFather
from donation.models import Donation
import braintree
from django.conf import settings
from django.contrib.auth.decorators import login_required

# instancia Braintree payment gateway
gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)

@login_required
def payment_done(request):
    return render(request, 'done.html')

@login_required
def payment_canceled(request):
    return render(request, 'canceled.html')

@login_required
def payment_process(request):
    # create and submit transaction
    if request.method == 'POST':
        # retrieve nonce
        nonce = request.POST.get('payment_method_nonce', None)
        total_cost = 150.00
        result = gateway.transaction.sale({
            'amount': f'{total_cost:.2f}',
            'payment_method_nonce': nonce,
            'options': {
            'submit_for_settlement': True
            }
        })
        if result.is_success:
            return redirect('done')
        else:
            return redirect('canceled')
    else:
        # generate token
        client_token = gateway.client_token.generate()
        return render(request,'process.html',{'client_token': client_token})

def index(request):
    if request.user.is_authenticated:
        if request.user.ong.name.lower() == "asem":
            view = 'index/index-asem.html'
            volunteers = Volunteer.objects.filter(ong=request.user.ong).count()
            users = ASEMUser.objects.filter(ong=request.user.ong).count()
            workers = Worker.objects.filter(ong=request.user.ong).count()
            donations = Donation.objects.filter(ong=request.user.ong).count()

            context = {
                'volunteers': volunteers,
                'users': users,
                'workers': workers,
                'donations': donations,
                'page_title': 'SarandONGa 💃 - Inicio'
            }
        elif request.user.ong.name.lower() == "videssur":
            view = 'index/index-videssur.html'
            volunteers = Volunteer.objects.filter(ong=request.user.ong).count()
            workers = Worker.objects.filter(ong=request.user.ong).count()
            donations = Donation.objects.filter(ong=request.user.ong).count()
            godfathers = GodFather.objects.filter(ong=request.user.ong).count()

            context = {
                'volunteers': volunteers,
                'workers': workers,
                'donations': donations,
                'godfathers': godfathers,
                'page_title': 'SarandONGa 💃 - Inicio'
            }
    else:
        view = 'index.html'
        context = {'page_title': 'SarandONGa 💃 - Inicio'}

    return render(request, view, context)


def components(request):

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

    context = {
        'options1': {'1':'1','2':'2','3':'3','4':'4'},
        'options2': {'4':'5','9':'8'},
        'stockTest': {'name':'STOCKINGS','quantity':9999},
        'object_name': 'ejemplo',
        'events_json': json.dumps(events),
    }

    return render(request, 'components.html', context)


def custom_403(request):
    return render(request, 'error/403.html', {}, status=403)

def asem_required(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if request.user.ong.name.lower() == "asem":
            return function(request, *args, **kwargs)
        else:
            messages.error(request, "Necesitas pertenecer a ASEM para acceder a esos datos")
            return custom_403(request)
    return wrapper

    
def videssur_required(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if request.user.ong.name.lower() == "videssur":
            return function(request, *args, **kwargs)
        else:
            messages.error(request, "Necesitas pertenecer a VidesSur para acceder a esos datos")
            return custom_403(request)
    return wrapper



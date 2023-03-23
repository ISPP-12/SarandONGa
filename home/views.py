from django.shortcuts import render, redirect
from django.contrib import messages
import json
from .models import Home
from .models import PAYMENT_METHOD
from .models import FREQUENCY
from .forms import CreateHomeForm
from decimal import Decimal
from datetime import date


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.strftime('%d/%m/%Y')
        elif isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


def home_create(request):
    if request.method == 'POST':
        form = CreateHomeForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, 'El formulario presenta errores')
    else:
        form = CreateHomeForm()
    return render(request, 'home/home_form.html', {'form': form})


def home_list(request):
    # get donations dict from database
    homes = Home.objects.all()

    homes_dict = [obj.__dict__ for obj in homes]
    for d in homes_dict:
        d.pop('_state', None)

    # choices to values
    for home in homes_dict:
        home['payment_method'] = dict(PAYMENT_METHOD)[home['payment_method']]
        home['frequency'] = dict(FREQUENCY)[home['frequency']]

    # json
    homes_json = json.dumps(homes_dict, cls=CustomJSONEncoder)

    context = {
        'objects': homes_dict,
        'objects_json': homes_json,
        'object_name': 'casa',
        'object_name_en': 'home',
        'title': 'Lista de Casas',
    }

    return render(request, 'home/list.html', context)


def home_delete(request, slug=None):
    home = Home.objects.get(slug=slug)
    home.delete()
    return redirect('home_list')

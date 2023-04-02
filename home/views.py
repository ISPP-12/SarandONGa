from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import json
from .models import Home
from .models import PAYMENT_METHOD
from .models import FREQUENCY
from .forms import CreateHomeForm
from decimal import Decimal
from datetime import date
from django.contrib.auth.decorators import login_required
from main.views import videssur_required
from xml.dom import ValidationErr


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.strftime('%d/%m/%Y')
        elif isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


@login_required
@videssur_required
def home_create(request):
    form = CreateHomeForm()
    if request.method == 'POST':
        form = CreateHomeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home_list')
            except ValidationErr as v:
                messages.error(request, str(v.args[0]))
        else:
            messages.error(request, 'El formulario presenta errores')
    return render(request, 'home/home_form.html', {'form': form})

@login_required
@videssur_required
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
        'title': 'Gestión de Casas',
    }

    return render(request, 'home/list.html', context)


@login_required
@videssur_required
def home_delete(request, home_id):
    home = get_object_or_404(Home, id=home_id)
    home.delete()
    return redirect('home_list')


@login_required
@videssur_required
def home_details(request, home_id):
    home = get_object_or_404(Home, id=home_id)
    return render(request, 'home/home_details.html', {'home': home})

@login_required
@videssur_required
def home_update(request,home_id):
    home_to_update = Home.objects.get(id=home_id)
    form = CreateHomeForm(instance=home_to_update)
    if request.method == "POST":
        form = CreateHomeForm(request.POST, instance=home_to_update)
        if form.is_valid():
            try:
                form.save()
                return redirect('home_list')
            except ValidationErr as v:
                    messages.error(request, str(v.args[0]))
        else:
            messages.error(request, 'Formulario con errores')
    return render(request, 'home/home_form.html', {"form": form})

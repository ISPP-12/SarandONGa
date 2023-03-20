from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
import json
from donation.models import Donation
from decimal import Decimal
from django.contrib import messages
from .forms import CreateNewDonation

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%d/%m/%Y')
        elif isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


# Create your views here.
def donation_create(request):
    if request.user.is_anonymous:
        form= CreateNewDonation()
        print("anonimo")
    else:
        form = CreateNewDonation(initial={'ong': request.user.ong})
    if request.method == "POST":
        form = CreateNewDonation(request.POST)

        if form.is_valid():
            ong=request.user.ong
            donation=form.save()
            donation.ong=ong
            donation.save()
            

            return redirect("/donation/list")
        else:
            messages.error(request, 'Formulario con errores')

    
    return render(request, 'donation/create.html', {'object_name': 'donate', "form": form, "button_text": "Registrar donación"})

def donation_list(request):
    # get donations from database
    donations = Donation.objects.all()

    donations_dict = [obj.__dict__ for obj in donations]
    for d in donations_dict:
        d.pop('_state', None)

    donations_json = json.dumps(donations_dict, cls=CustomJSONEncoder)

    for donation in donations:
        created_date = donation.created_date
        modified_date = created_date.strftime('%d/%m/%Y')
        donation.created_date = modified_date

    context = {
        'objects': donations,
        'objects_json': donations_json,
        'object_name': 'donación',
        'object_name_en': 'donation',
        'title': 'Gestión de donaciones',
        }

    return render(request, 'donation/list.html', context)

def donation_update(request, donation_id):

    donation = get_object_or_404(Donation, id=donation_id)
    form = CreateNewDonation(instance = donation)

    if request.method == "POST":
        form = CreateNewDonation(request.POST, instance = donation)
        if form.is_valid():
            form.save()

            return redirect('/donation/list')

    return render(request, 'donation/create.html', {'object_name': 'donate', "form": form, "button_text": "Actualizar"})
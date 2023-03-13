from django.shortcuts import render
from datetime import datetime
import json
from donation.models import Donation
from decimal import Decimal
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
    if request.method == "POST":
        form = CreateNewDonation(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            created_date = form.cleaned_data["created_date"]
            amount = form.cleaned_data["amount"]
            donor_name = form.cleaned_data["donor_name"]
            donor_surname = form.cleaned_data["donor_surname"]
            donor_dni = form.cleaned_data["donor_dni"]
            donor_address = form.cleaned_data["donor_address"]
            donor_email = form.cleaned_data["donor_email"]
            d = Donation(title= title, description=description, created_date=created_date,
                        amount=amount, donor_name=donor_name, donor_surname=donor_surname, donor_dni=donor_dni,
                        donor_address=donor_address, donor_email=donor_email)
            d.save()

    form = CreateNewDonation()
    return render(request, 'donation_form.html', {"form": form})

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
        'title': 'Gestión de donaciones',
        'search_text': 'Buscar donación...',
        }

    return render(request, 'donation/list.html', context)

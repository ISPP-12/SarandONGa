from django.shortcuts import render
from .models import Subsidy
from .forms import CreateNewSubsidy
from datetime import date
import json
from decimal import Decimal


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.strftime('%d/%m/%Y')
        elif isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


def subsidy_create(request):
    if request.method == "POST":
        form = CreateNewSubsidy(request.POST)
        if form.is_valid():
            form.save()

    form = CreateNewSubsidy()
    return render(request, 'subsidy_form.html', {"form": form, "title": "Crear Subvención"})


def subsidy_list(request):
    subsidies = Subsidy.objects.all()

    subsidies_dict = [obj.__dict__ for obj in subsidies]
    for s in subsidies_dict:
        s.pop('_state', None)

    subsidies_json = json.dumps(subsidies_dict, cls=CustomJSONEncoder)

    for subsidy in subsidies:
        date1 = subsidy.presentation_date
        date2 = subsidy.payment_date
        modified_date1 = date1.strftime('%d/%m/%Y')
        modified_date2 = date2.strftime('%d/%m/%Y')
        subsidy.presentation_date = modified_date1
        subsidy.payment_date = modified_date2

    context = {
        'objects': subsidies,
        'objects_json': subsidies_json,
        'object_name': 'subvención',
        'object_name_en': 'subsidy',
        'title': 'Listado de Subvenciones',
        }

    return render(request, 'subsidy/list.html', context)

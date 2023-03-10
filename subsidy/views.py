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


def subsidy(request):
    if request.method == "POST":
        form = CreateNewSubsidy(request.POST)
        if form.is_valid():
            form.save()

    form = CreateNewSubsidy()
    return render(request, 'subsidy_form.html', {"form": form})


def subsidies_list(request):
    subsidies = Subsidy.objects.all()
    objects_name = 'Subvención'
    title = 'Listado de Subvenciones'

    subsidies_dict = [obj.__dict__ for obj in subsidies]
    for s in subsidies_dict:
        s.pop('_state', None)

    subsidies_json = json.dumps(subsidies_dict, cls=CustomJSONEncoder)

    for subsidy in subsidies:
        date = subsidy.date
        modified_date = date.strftime('%d/%m/%Y')
        subsidy.date = modified_date

    context = {
        'objects': subsidies,
        'objects_json': subsidies_json,
        'objects_name': objects_name,
        'title': title
        }

    return render(request, 'subsidy/list.html', context)

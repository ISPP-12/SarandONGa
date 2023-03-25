from django.shortcuts import render, redirect, get_object_or_404
from .models import Subsidy
from .forms import CreateNewSubsidy
from datetime import date
import json
from decimal import Decimal
from django.contrib import messages
from django.contrib.auth.decorators import login_required



class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.strftime('%d/%m/%Y')
        elif isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)

@login_required(login_url='/admin/login/?next=/user/subsidy/create/')
def subsidy_create(request):
  
    form = CreateNewSubsidy(initial={'ong': request.user.ong})
    if request.method == "POST":
        form = CreateNewSubsidy(request.POST)

        if form.is_valid():
            ong=request.user.ong
            subsidy=form.save(commit=False)
            subsidy.ong=ong
            subsidy.save()
            

            return redirect("/subsidy/list")
        else:
            messages.error(request, 'Formulario con errores')

    return render(request, 'subsidy/create.html', {"form": form,"object_name":"subvención" ,  "title": "Añadir Subvención"})


def subsidy_list(request):
    subsidies = Subsidy.objects.all()

    subsidies_dict = [obj.__dict__ for obj in subsidies]
    for s in subsidies_dict:
        s.pop('_state', None)

    subsidies_json = json.dumps(subsidies_dict, cls=CustomJSONEncoder)

    context = {
        'objects': subsidies,
        'objects_json': subsidies_json,
        'object_name': 'subvención',
        'object_name_en': 'subsidy',
        'title': 'Listado de Subvenciones',
    }

    return render(request, 'subsidy/list.html', context)


def subsidy_delete(request, subsidy_id):
    subsidy = get_object_or_404(Subsidy, id=subsidy_id)
    subsidy.delete()
    return redirect("/subsidy/list")

@login_required(login_url='/admin/login/?next=/user/subsidy/create/')
def subsidy_update(request, subsidy_id):
    subsidy = get_object_or_404(Subsidy, id=subsidy_id)
    
    
    form= CreateNewSubsidy(instance=subsidy)
    if request.method == "POST":
        form= CreateNewSubsidy(request.POST or None, instance=subsidy)
        if form.is_valid():
            form.save()
            return redirect("/subsidy/list")
        else:
            messages.error(request, 'Formulario con errores')
    return render(request, 'subsidy/create.html', {"form": form})


     
from django.shortcuts import render, redirect, get_object_or_404
from .models import Subsidy
from .forms import CreateNewSubsidy
from datetime import date
import json
from decimal import Decimal
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from main.views import custom_403



class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.strftime('%d/%m/%Y')
        elif isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)

@login_required
 
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

@login_required
 
def subsidy_list(request):
    subsidies = Subsidy.objects.filter(ong=request.user.ong).values()

    paginator = Paginator(subsidies, 12)
    page_number = request.GET.get('page')
    subsidy_page = paginator.get_page(page_number)

    subsidies_dict = [obj for obj in subsidy_page]
    for s in subsidies_dict:
        s.pop('_state', None)

    subsidies_json = json.dumps(subsidies_dict, cls=CustomJSONEncoder)

    context = {
        'objects': subsidy_page,
        'objects_json': subsidies_json,
        'object_name': 'subvención',
        'object_name_en': 'subsidy',
        'title': 'Gestión de Subvenciones',
    }

    return render(request, 'subsidy/list.html', context)

@login_required
 
def subsidy_delete(request, subsidy_id):
    subsidy = get_object_or_404(Subsidy, id=subsidy_id)
    if subsidy.ong == request.user.ong:
        subsidy.delete()
    else:
       return custom_403(request)
    return redirect("/subsidy/list")

@login_required
 
def subsidy_update(request, subsidy_id):
    subsidy = get_object_or_404(Subsidy, id=subsidy_id)
    
    
    if request.user.ong == subsidy.ong:
        form= CreateNewSubsidy(instance=subsidy)
        if request.method == "POST":
            form= CreateNewSubsidy(request.POST or None, instance=subsidy)
            if form.is_valid():
                form.save()
                return redirect("/subsidy/list")
            else:
                messages.error(request, 'Formulario con errores')
    else:
        return custom_403(request)
    return render(request, 'subsidy/create.html', {"form": form})


     

from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewProyect
from django.contrib import messages
from proyect.models import Proyect
from datetime import date
from decimal import Decimal
import json

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.strftime('%d/%m/%Y')
        elif isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)
    
def proyect_delete(request, proyect_id):
    proyect = get_object_or_404(Proyect, id=proyect_id)
    proyect.delete()
    return redirect('/')

def proyect_list(request):
    proyects = Proyect.objects.all()

    proyects_dict = [obj.__dict__ for obj in proyects]
    for d in proyects_dict:
        d.pop('_state', None)

    proyects_json = json.dumps(proyects_dict, cls=CustomJSONEncoder)

    context = {
        'objects': proyects,
        'objects_json': proyects_json,
        'object_name': 'proyecto',
        'object_name_en': 'proyect',
        'title': 'Gestión de proyectos',
        }
    
    return render(request, 'proyect/list.html', context)

def proyect_create(request):
    if request.method == "POST":
        form = CreateNewProyect(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    form = CreateNewProyect()
    return render(request, 'proyect/proyect_form.html', {"form": form, "title": "Crear Proyecto"})


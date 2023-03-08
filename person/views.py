import json
from django.shortcuts import render

from person.models import GodFather

# Create your views here.

def show_workers(request):
    #Get all persons
    workers = GodFather.objects.all()
    return render(request, 'workers.html', {"objects": workers, "objects_json": json.dumps(workers), "object_name": "Trabajadores", "title": "Listado de trabajadores"})

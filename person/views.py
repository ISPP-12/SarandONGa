from django.shortcuts import render
from .models import GodFather, ASEMUser, Worker, Child, Volunteer
from django.contrib import messages
import json
from datetime import datetime
from decimal import Decimal
from .forms import CreateNewGodFather, CreateNewASEMUser,CreateNewWorker, CreateNewChild

def godfather_list(request):

    context = {
        'objects': GodFather.objects.all(),
        #'objects_json' : json.dumps(list(GodFather.objects.all().values())),
        'objects_name': 'Padrino',
        'title': 'Gestión de padrinos'
    }
    return render(request, 'person/godfather_list.html', {"context":context})

def asem_user(request):
    if request.method == "POST":
        form = CreateNewASEMUser(request.POST)
        if form.is_valid():
            form.save()

    form = CreateNewASEMUser()
    return render(request, 'asem_user/asem_user_form.html', {"form": form})


def asem_user_list(request):
    objects = ASEMUser.objects.all().values()
    # objects_json = json.dumps(objects)
    object_name = 'usuario'
    title = "Gestion de Usuarios ASEM"
    return render(request, 'asem_user_list.html', {"objects": objects, "objects_name": object_name, "title": title})


def create_worker(request):
    if request.method == "POST":
        form = CreateNewWorker(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, 'Formulario con errores')

    form = CreateNewWorker()
    return render(request, 'worker/worker_form.html', {"form": form})


def workers_list(request):
    workers = Worker.objects.all()
    # object_json = json.dumps(workers)
    return render(request, 'workers.html', {"objects": workers, "object_name": "Trabajadores", "title": "Listado de trabajadores"})


def children_list(request):
    children = Child.objects.all()
    # object_json = json.dumps(children)
    return render(request, 'children_list.html', {"objects": children, "object_name": "Niños", "title": "Listado de niños"})


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%d/%m/%Y')
        elif isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


def user_list(request):
    objects = ASEMUser.objects.all().values()
    title = "Gestion de Trabajadores"
    #depending of the user type write one title or another
    persons_dict = [obj for obj in objects]
    for d in persons_dict:
        d.pop('_state', None)

    persons_json = json.dumps(persons_dict, cls=CustomJSONEncoder)
    return render(request, 'users/list.html', {'objects': objects, 'object_name': 'usuario', 'title': title, 'objects_json': persons_json})


def godfather_create(request):
    if request.method == "POST":
        form = CreateNewGodFather(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, 'Formulario con errores')

    form = CreateNewGodFather()
    return render(request, 'godfather_form.html', {"form": form})


def create_child(request):
    if request.method == "POST":
        form = CreateNewChild(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, 'Formulario con errores')
    else:
        form = CreateNewChild()
    return render(request, 'person/child/create_child.html', {"form": form})
    
def volunteers_list(request):
    volunteers = Volunteer.objects.all().values()
    # object_json = json.dumps(volunteers)
    return render(request, 'volunteers.html', {"objects": volunteers,"object_name": "Voluntarios", "title": "Listado de Voluntarios"})

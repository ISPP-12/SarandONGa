from django.shortcuts import render
from .models import GodFather, ASEMUser, Worker
from .forms import CreateNewASEMUser,CreateNewWorker
from django.contrib import messages
#import json

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
    return render(request, 'workers.html', {"objects": workers,"object_name": "Trabajadores", "title": "Listado de trabajadores"})


from django.shortcuts import render,redirect
from .models import GodFather, ASEMUser, Worker, Child, Volunteer
from django.contrib import messages
import json
from datetime import datetime,date
from decimal import Decimal
from .forms import CreateNewGodFather, CreateNewASEMUser,CreateNewWorker, CreateNewChild


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%d/%m/%Y')
        elif isinstance(obj, date):
            return obj.strftime('%d/%m/%Y')
        elif isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


def godfather_list(request):
    objects = GodFather.objects.all().values()
    title = "Gestion de Padrinos"
    #depending of the user type write one title or another
    persons_dict = [obj for obj in objects]
    for d in persons_dict:
        d.pop('_state', None)

    persons_json = json.dumps(persons_dict, cls=CustomJSONEncoder)

    context = {
        'objects': objects,
        'object_name': 'Padrino',
        'title': title,
        'objects_json': persons_json,
        }

    return render(request, 'users/list.html', context)


def user_create(request):
    if request.method == "POST":
        form = CreateNewASEMUser(request.POST)
        if form.is_valid():

            form.save()
            return redirect('user_list')
    form = CreateNewASEMUser()
    return render(request, 'asem_user/asem_user_form.html', {"form": form})



def worker_create(request):
    if request.method == "POST":
        form = CreateNewWorker(request.POST)
        if form.is_valid():
            form.save()
            return redirect('worker_list')

        else:
            messages.error(request, 'Formulario con errores')

    form = CreateNewWorker()
    return render(request, 'worker/worker_form.html', {"form": form})


def worker_list(request):
    objects = Worker.objects.all().values()
    title = "Gestion de Trabajadores"
    #depending of the user type write one title or another
    persons_dict = [obj for obj in objects]
    for d in persons_dict:
        d.pop('_state', None)

    persons_json = json.dumps(persons_dict, cls=CustomJSONEncoder)

    context = {
        'objects': objects,
        'object_name': 'Trabajador',
        'title': title,
        'objects_json': persons_json,
        }

    return render(request, 'users/list.html', context)

def child_list(request):
    objects = Child.objects.all().values()
    title = "Gestion de Niños"
    #depending of the user type write one title or another
    persons_dict = [obj for obj in objects]
    for d in persons_dict:
        d.pop('_state', None)

    persons_json = json.dumps(persons_dict, cls=CustomJSONEncoder)

    context = {
        'objects': objects, 
        'object_name': 'Niño', 
        'title': title, 
        'objects_json': persons_json,
        }

    return render(request, 'users/list.html', context)


def user_list(request):
    objects = ASEMUser.objects.all().values()
    title = "Gestion de Usuarios ASEM"
    #depending of the user type write one title or another
    persons_dict = [obj for obj in objects]
    for d in persons_dict:
        d.pop('_state', None)

    persons_json = json.dumps(persons_dict, cls=CustomJSONEncoder)

    context = {
        'objects': objects,
        'object_name': 'Usuario',
        'title': title,
        'objects_json': persons_json,
        }

    return render(request, 'users/list.html', context)


def godfather_create(request):
    if request.method == "POST":
        form = CreateNewGodFather(request.POST)
        print(form.errors)

        if form.is_valid():
            form.save()
            return redirect('godfather_list')
        else:
            messages.error(request, 'Formulario con errores')

    form = CreateNewGodFather()
    return render(request, 'godfather_form.html', {"form": form})


def child_create(request):
    if request.method == "POST":
        form = CreateNewChild(request.POST)
        if form.is_valid():
            form.save()
            return redirect('child_list')
        else:
            messages.error(request, 'Formulario con errores')
    else:
        form = CreateNewChild()
    return render(request, 'person/child/create_child.html', {"form": form})


def volunteer_list(request):
    objects = Volunteer.objects.all().values()
    title = "Gestion de Voluntarios"
    #depending of the user type write one title or another
    persons_dict = [obj for obj in objects]
    for d in persons_dict:
        d.pop('_state', None)

    persons_json = json.dumps(persons_dict, cls=CustomJSONEncoder)

    context = {
        'objects': objects,
        'object_name': 'Voluntario',
        'title': title,
        'objects_json': persons_json,
        'search_text': 'Buscar voluntario...',
        }

    return render(request, 'users/list.html', context)

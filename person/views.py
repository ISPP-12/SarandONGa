from django.shortcuts import render, redirect, get_object_or_404
from .models import GodFather, ASEMUser, Worker, Child, Volunteer
from django.contrib import messages
import json
from datetime import datetime, date
from decimal import Decimal
from .forms import CreateNewGodFather, CreateNewASEMUser, CreateNewVolunteer, CreateNewWorker, CreateNewChild


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
    # depending of the user type write one title or another
    persons_dict = [obj for obj in objects]
    for d in persons_dict:
        d.pop('_state', None)

    persons_json = json.dumps(persons_dict, cls=CustomJSONEncoder)

    context = {
        'objects': objects,
        'object_name': 'padrino',
        'object_name_en': 'godfather',
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
    return render(request, 'asem_user/asem_user_form.html', {"form": form, "title": "Añadir Usuario ASEM"})


def worker_create(request):
    if request.method == "POST":
        form = CreateNewWorker(request.POST)
        if form.is_valid():
            form.save()
            return redirect('worker_list')

        else:
            messages.error(request, 'Formulario con errores')

    form = CreateNewWorker()
    return render(request, 'worker/worker_form.html', {"form": form, "title": "Añadir Trabajador"})


def worker_list(request):
    objects = Worker.objects.all().values()
    title = "Gestion de Trabajadores"
    # depending of the user type write one title or another
    persons_dict = [obj for obj in objects]
    for d in persons_dict:
        d.pop('_state', None)

    persons_json = json.dumps(persons_dict, cls=CustomJSONEncoder)

    context = {
        'objects': objects,
        'object_name': 'trabajador',
        'object_name_en': 'worker',
        'title': title,
        'objects_json': persons_json,
    }

    return render(request, 'users/list.html', context)


def child_list(request):
    objects = Child.objects.all().values()
    title = "Gestion de Niños"
    # depending of the user type write one title or another
    persons_dict = [obj for obj in objects]
    for d in persons_dict:
        d.pop('_state', None)

    persons_json = json.dumps(persons_dict, cls=CustomJSONEncoder)

    context = {
        'objects': objects,
        'object_name': 'niño',
        'object_name_en': 'child',
        'title': title,
        'objects_json': persons_json,
    }

    return render(request, 'users/list.html', context)


def user_list(request):
    objects = ASEMUser.objects.all().values()
    title = "Gestion de Usuarios ASEM"
    # depending of the user type write one title or another
    persons_dict = [obj for obj in objects]
    for d in persons_dict:
        d.pop('_state', None)

    persons_json = json.dumps(persons_dict, cls=CustomJSONEncoder)

    context = {
        'objects': objects,
        'object_name': 'usuario',
        'object_name_en': 'user',
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
    return render(request, 'godfather_form.html', {"form": form, "title": "Añadir Padrino"})


def godfather_details(request, godfather_id):
    godfather = get_object_or_404(GodFather, id=godfather_id)
    return render(request, 'prueba_padrino_detalles.html', {'godfather': godfather})


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
    return render(request, 'person/child/create_child.html', {"form": form, "title": "Añadir Niño"})

def child_details(request, child_id):
    child = get_object_or_404(Child, id=child_id)
    return render(request, 'child_details.html', {'child': child})

def volunteer_list(request):
    objects = Volunteer.objects.all().values()
    title = "Gestion de Voluntarios"
    # depending of the user type write one title or another
    persons_dict = [obj for obj in objects]
    for d in persons_dict:
        d.pop('_state', None)

    persons_json = json.dumps(persons_dict, cls=CustomJSONEncoder)

    context = {
        'objects': objects,
        'object_name': 'voluntario',
        'object_name_en': 'volunteer',
        'title': title,
        'objects_json': persons_json,
        'search_text': 'Buscar voluntario...',
    }

    return render(request, 'users/list.html', context)


def volunteer_create(request):
    if request.method == "POST":
        form = CreateNewVolunteer(request.POST)
        if form.is_valid():
            form.save()
            return redirect('volunteer_list')
        else:
            messages.error(request, 'Formulario con errores')

    form = CreateNewVolunteer()
    return render(request, 'volunteers/volunteers_form.html', {"form": form, "title": "Añadir Voluntario"})

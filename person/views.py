from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import GodFather, ASEMUser, Worker, Child, Volunteer, SEX_TYPES, PAYMENT_METHOD, STATUS, FREQUENCY, CONDITION, MEMBER, ASEMUSER_TYPE, CORRESPONDENCE, HOUSING_TYPE, VOLUNTEER_TYPE
from django.contrib import messages
import json
from datetime import datetime, date
from decimal import Decimal

from .forms import CreateNewGodFather, CreateNewASEMUser, CreateNewVolunteer, CreateNewWorker, CreateNewChild, UpdateWorker
from xml.dom import ValidationErr



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

def asem_user_delete(request, asem_user_id):
    asemuser = get_object_or_404(ASEMUser, id=asem_user_id)
    asemuser.delete()
    return redirect('user_list')

def user_update(request, asem_user_id):
    asem_user = get_object_or_404(ASEMUser, id=asem_user_id)
    if request.method == "POST":
        form = CreateNewASEMUser(request.POST, instance=asem_user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        else:
            messages.error(request, 'Formulario con errores')

    form = CreateNewASEMUser(instance=asem_user)
    return render(request, 'asem_user/asem_user_form.html', {"form": form})

def choices_dicts():
    choices_dict = {
    'sex_types': dict(SEX_TYPES),
    'payment_method': dict(PAYMENT_METHOD),
    'status': dict(STATUS),
    'frequency': dict(FREQUENCY),
    'condition': dict(CONDITION),
    'member': dict(MEMBER),
    'asemuser_type': dict(ASEMUSER_TYPE),
    'correspondence': dict(CORRESPONDENCE),
    'housing_type': dict(HOUSING_TYPE),
    'volunteer_type': dict(VOLUNTEER_TYPE)
    }
    return choices_dict

def asem_user_details(request, asem_user_id):
    asem_user = get_object_or_404(ASEMUser, id=asem_user_id)
    
    choices_dict = choices_dicts()
    asem_user.condition = choices_dict['condition'][asem_user.condition]
    asem_user.member = choices_dict['member'][asem_user.member]
    asem_user.correspondence = choices_dict['correspondence'][asem_user.correspondence]
    asem_user.user_type = choices_dict['asemuser_type'][asem_user.user_type]
    asem_user.status = choices_dict['status'][asem_user.status]
    asem_user.own_home = choices_dict['housing_type'][asem_user.own_home]

    return render(request, 'asem_user/asem_user_details.html', {'asem_user': asem_user})


def worker_create(request):
    if request.method == "POST":
        form = CreateNewWorker(request.POST)
        if form.is_valid():
            form.save()
            return redirect('worker_list')

        else:
            messages.error(request, 'Formulario con errores')

    form = CreateNewWorker()
    return render(request, 'worker/worker_create_form.html', {"form": form, "title": "Añadir Trabajador"})

def worker_update(request, worker_id):
    worker = get_object_or_404(Worker, id=worker_id)
    if request.method == "POST":
        form = UpdateWorker(request.POST, instance=worker)
        if form.is_valid():
            form.save()
            return redirect('worker_list')
        else:
            messages.error(request, 'Formulario con errores')

    form = UpdateWorker(instance=worker)
    return render(request, 'worker/worker_update_form.html', {"form": form, "title": "Actualizar Trabajador"})

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

def worker_details(request, worker_id):
    worker = get_object_or_404(Worker, id=worker_id)
    return render(request, 'worker/details.html', {'worker': worker})

def worker_delete(request, worker_id):
    worker = get_object_or_404(Worker, id=worker_id)
    worker.delete()
    return redirect('worker_list')

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
            try:
                godfather=form.save(commit=False)
                godfather.dni=request.POST["dni"]
                godfather.bank_account_number=request.POST["bank_account_number"]
                godfather.save()
                return redirect('godfather_list')
            except ValidationErr as v:
                messages.error(request, str(v.args[0]))
        else:
            messages.error(request, 'Formulario con errores')

    form = CreateNewGodFather()
    return render(request, 'godfather_form.html', {"form": form, "title": "Añadir Padrino"})

def godfather_update(request,godfather_slug):
    godfather= get_object_or_404(GodFather, slug=godfather_slug)
    data={'email': godfather.email,
          'name': godfather.name,
          'surname': godfather.surname,
          'birth_date': godfather.birth_date,
          'sex': godfather.sex,
          'city': godfather.city,
          'address': godfather.address,
          'telephone': godfather.telephone,
          'postal_code': godfather.postal_code,
          'photo': godfather.photo,
          'dni': godfather.dni,
          'payment_method': godfather.payment_method,
          'bank_account_number': godfather.bank_account_number,
          'bank_account_holder': godfather.bank_account_holder,
          'bank_account_reference': godfather.bank_account_reference,
          'amount': godfather.amount,
          'frequency': godfather.frequency,
          'start_date': godfather.start_date,
          'termination_date': godfather.termination_date,
          'notes': godfather.notes,
          'status': godfather.status,
          'ong': godfather.ong}

    form= CreateNewGodFather(instance=godfather,data=data)
    if request.method == "POST":
        form= CreateNewGodFather(request.POST or None,request.FILES or None ,instance=godfather)
        if form.is_valid():
            try:
                form.save(commit=False)
                godfather.dni=request.POST["dni"]
                godfather.bank_account_number=request.POST["bank_account_number"]
                godfather.save()
                return redirect("godfather_list")
            except ValidationErr as v:
                messages.error(request, str(v.args[0]))
        else:
            messages.error(request, 'Formulario con errores')
    return render(request, 'godfather_form.html', {"form": form})


def godfather_details(request, godfather_id):
    godfather = get_object_or_404(GodFather, id=godfather_id)
    return render(request, 'prueba_padrino_detalles.html', {'godfather': godfather})


def child_create(request):
    if request.method == "POST":
        form = CreateNewChild(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('child_list')
            except ValidationErr as v:
                messages.error(request, str(v.args[0]))
        else:
            messages.error(request, 'Formulario con errores')
    else:
        form = CreateNewChild()
    return render(request, 'person/child/create_child.html', {"form": form, "title": "Añadir Niño"})


def child_update(request,child_slug):
    child= get_object_or_404(Child, slug=child_slug)

    form= CreateNewChild(instance=child)
    if request.method == "POST":
        form= CreateNewChild(request.POST or None,request.FILES or None ,instance=child)
        if form.is_valid():
            try:
                form.save()
                return redirect("child_list")
            except ValidationErr as v:
                messages.error(request, str(v.args[0]))
        else:
            messages.error(request, 'Formulario con errores')
    return render(request, 'person/child/create_child.html', {"form": form})


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

def volunteer_details(request, volunteer_id):
    volunteer = get_object_or_404(Volunteer, id=volunteer_id)
    return render(request, 'volunteer_details.html', {'volunteer': volunteer})

@login_required(login_url='/admin/login/?next=/user/volunteer/create/')
def volunteer_create(request):
    form = CreateNewVolunteer(initial={'ong':request.user.ong})

    if request.method == "POST":
        form = CreateNewVolunteer(request.POST)

        if form.is_valid():
            ong = request.user.ong
            # if the user is anonymous, the ong is not set yet. Actually, it won't be possible to create a volunteer unless the user is logged in
            volunteer = form.save(commit=False)
            volunteer.ong = ong
            volunteer.save()
            return redirect('volunteer_list')
        else:
            messages.error(request, 'Formulario con errores')
    return render(request, 'volunteers/volunteers_form.html', {"form": form, "title": "Añadir Voluntario"})

def volunteer_delete(request, volunteer_id):
    volunteer = Volunteer.objects.get(id=volunteer_id)
    volunteer.delete()
    return redirect('volunteer_list')

def volunteer_update(request, volunteer_id):
    volunteer = get_object_or_404(Volunteer, id=volunteer_id)
    if request.method == "POST":
        form = CreateNewVolunteer(request.POST, instance=volunteer)
        if form.is_valid():
            form.save()
            return redirect('volunteer_list')
        else:
            messages.error(request, 'Formulario con errores')

    form = CreateNewVolunteer(instance=volunteer)
    return render(request, 'volunteers/volunteers_form.html', {"form": form})
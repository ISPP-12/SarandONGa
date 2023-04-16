from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from sponsorship.models import Sponsorship
from .models import GodFather, ASEMUser, Worker, Child, Volunteer, SEX_TYPES, PAYMENT_METHOD, STATUS, FREQUENCY, CONDITION, MEMBER, ASEMUSER_TYPE, CORRESPONDENCE, HOUSING_TYPE, VOLUNTEER_TYPE
from django.contrib import messages
import json
from datetime import datetime, date
from decimal import Decimal
from main.views import videssur_required, asem_required, custom_403
from .forms import CreateNewGodFather, CreateNewASEMUser, CreateNewVolunteer, CreateNewWorker, CreateNewChild, UpdateWorker, FilterAsemUserForm, FilterWorkerForm, FilterVolunteerForm, FilterGodfatherForm, FilterChildForm
from xml.dom import ValidationErr
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from dateutil.relativedelta import relativedelta
import math
from django.http import HttpResponse
import csv


class UpdatePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('worker_list')
    template_name = 'update_password.html'


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%d/%m/%Y')
        elif isinstance(obj, date):
            return obj.strftime('%d/%m/%Y')
        elif isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


@login_required
@videssur_required
def godfather_list(request):
    objects = GodFather.objects.filter(ong=request.user.ong).values()
    page_title = 'SarandONGa 💃 - Gestión de Padrinos'
    title = "Gestión de Padrinos"

    form = FilterGodfatherForm(request.GET or None)
    objects = godfather_filter(objects, form)

    paginator = Paginator(objects, 12)
    page_number = request.GET.get('page')
    godfather_page = paginator.get_page(page_number)

    # depending of the user type write one title or another
    persons_dict = [obj for obj in godfather_page]
    for person in persons_dict:
        person.pop('_state', None)
        # remove null values
        for key, value in list(person.items()):
            if value is None or value == '':
                person[key] = '-'

    persons_json = json.dumps(persons_dict, cls=CustomJSONEncoder)

    context = {
        'objects': godfather_page,
        'object_name': 'padrino',
        'object_name_en': 'godfather',
        'page_title': page_title,
        'title': title,
        'objects_json': persons_json,
        'form': form,
    }

    return render(request, 'person/users/list.html', context)


def godfather_filter(queryset, form):

    q = form['qsearch'].value()
    birth_date_min = form['birth_date_min'].value()
    birth_date_max = form['birth_date_max'].value()
    sex = form['sex'].value()
    status = form['status'].value()

    if q is not None:
        if q.strip() != "":
            queryset = queryset.filter(
                Q(name__icontains=q) |
                Q(surname__icontains=q) |
                Q(address__icontains=q) |
                Q(city__icontains=q) |
                Q(postal_code__icontains=q) |
                Q(email__icontains=q) |
                Q(telephone__icontains=q) |
                Q(birth_date__icontains=q) |
                Q(sex__icontains=q) |
                Q(dni__icontains=q) |
                Q(payment_method__icontains=q) |
                Q(frequency__icontains=q) |
                Q(amount__icontains=q) |
                Q(bank_account_number__icontains=q) |
                Q(bank_account_holder__icontains=q) |
                Q(bank_account_reference__icontains=q) |
                Q(start_date__icontains=q) |
                Q(termination_date__icontains=q) |
                Q(notes__icontains=q) |
                Q(status__icontains=q)
            )

    if is_valid_queryparam(birth_date_min):
        queryset = queryset.filter(birth_date__gte=birth_date_min)

    if is_valid_queryparam(birth_date_max):
        queryset = queryset.filter(birth_date__lte=birth_date_max)

    if is_valid_queryparam(sex):
        queryset = queryset.filter(sex=sex)

    if is_valid_queryparam(status):
        queryset = queryset.filter(status=status)

    return queryset


@login_required
@asem_required
def user_create(request):
    form = CreateNewASEMUser(initial={'ong': request.user.ong})
    if request.method == 'POST':
        form = CreateNewASEMUser(request.POST, request.FILES)
        if form.is_valid():
            ong = request.user.ong  # basically, it is ASEM
            user = form.save(commit=False)
            user.ong = ong
            user.save()
            return redirect('user_list')
        else:
            messages.error(request, 'Formulario con errores')

    context = {
        "form": form, 
        "title": "Añadir Usuario ASEM", 
        'page_title': 'SarandONGa 💃 - Añadir Usuario ASEM'
        }

    return render(request, 'person/asem_user/register.html', context)


@login_required
@asem_required
def asem_user_delete(request, asem_user_id):
    asemuser = get_object_or_404(ASEMUser, id=asem_user_id)
    asemuser.delete()
    return redirect('user_list')


@login_required
@asem_required
def user_update(request, asem_user_id): 
    asem_user = get_object_or_404(ASEMUser, id=asem_user_id)
    if request.method == 'POST':
        form = CreateNewASEMUser(
            request.POST, request.FILES, instance=asem_user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        else:
            messages.error(request, 'Formulario con errores')

    form = CreateNewASEMUser(instance=asem_user)

    context = {
        'form': form, 
        'page_title': 'SarandONGa 💃 - Editar Usuario ASEM', 
        'title': 'Editar Usuario ASEM'
        }

    return render(request, 'person/asem_user/register.html', context)


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


@login_required
@asem_required
def asem_user_details(request, asem_user_id):
    asem_user = get_object_or_404(ASEMUser, id=asem_user_id)

    NOT_DEFINED = "No especificado"

    choices_dict = choices_dicts()
    asem_user.condition = choices_dict['condition'][asem_user.condition] if asem_user.condition else NOT_DEFINED
    asem_user.member = choices_dict['member'][asem_user.member] if asem_user.member else NOT_DEFINED
    asem_user.correspondence = choices_dict['correspondence'][
        asem_user.correspondence] if asem_user.correspondence else NOT_DEFINED
    asem_user.user_type = choices_dict['asemuser_type'][asem_user.user_type] if asem_user.user_type else NOT_DEFINED
    asem_user.status = choices_dict['status'][asem_user.status] if asem_user.status else NOT_DEFINED
    asem_user.own_home = choices_dict['housing_type'][asem_user.own_home] if asem_user.own_home else NOT_DEFINED

    fields = [f for f in ASEMUser._meta.get_fields() if f.name not in [
        'id', 'photo', 'password', 'user_type', 'name', 'surname', 'service', 'ong', 'person_ptr']]
    info = [getattr(asem_user, f.name) for f in fields]

    fields_info = dict(zip([f.verbose_name for f in fields], info))

    items = list(fields_info.items())

    for item in items:
        if ((item[1] == True or item[1] == 'True') and type(item[1]) != int):
            items[items.index(item)] = (item[0], 'Sí')
        elif ((item[1] == False or item[1] == 'False') and type(item[1]) != int):
            items[items.index(item)] = (item[0], 'No')
        elif (item[0] == 'Género' and item[1] != None):
            choices = ASEMUser._meta.get_field('sex').choices
            value = [choice[1]
                     for choice in choices if choice[0] == item[1]][0]
            items[items.index(item)] = (item[0], value)
        elif (item[0] == 'Tiempo de dedicación'):
            items[items.index(item)] = (item[0], str(item[1]) + ' horas')

    items = [item for item in items if item[1] !=
             None and item[1] != '' and item[1] != []]

    mid = math.ceil(len(items) / 2)

    page_title = 'SarandONGa 💃 - ' + asem_user.name + ' ' + asem_user.surname
    
    context = {
        'asem_user': asem_user, 
        'info_left': items[:mid], 
        'info_right': items[mid:], 
        'page_title': page_title
        }

    return render(request, 'person/users/details.html', context)


@login_required
def worker_create(request):
    form = CreateNewWorker(initial={'ong': request.user.ong})
    if request.method == 'POST':
        form = CreateNewWorker(request.POST, request.FILES)
        if form.is_valid():
            ong = request.user.ong
            worker = form.save(commit=False)
            worker.ong = ong
            worker.save()
            form.save()

            return redirect('worker_list')
        else:
            messages.error(request, 'Formulario con errores')

    context = {
        "form": form, 
        "title": "Añadir trabajador", 
        'page_title': 'SarandONGa 💃 - Añadir Trabajador'
        }

    return render(request, 'person/workers/register.html', context)


@login_required
def worker_update(request, worker_id): 
    worker = get_object_or_404(Worker, id=worker_id)
    if request.user.ong == worker.ong:
        if request.method == 'POST':
            form = UpdateWorker(request.POST, request.FILES, instance=worker)
            if form.is_valid():
                form.save()
                return redirect('worker_list')
            else:
                messages.error(request, 'Formulario con errores')

        form = UpdateWorker(instance=worker)
        context = {'form': form, 'title': 'Actualizar Trabajador', 'page_title': 'SarandONGa 💃 - Actualizar Trabajador'}
    else:
        return custom_403(request)
    return render(request, 'person/workers/register.html', context)


@login_required
def worker_list(request):
    objects = Worker.objects.filter(ong=request.user.ong).values()
    title = 'Gestión de Trabajadores'
    form = FilterWorkerForm(request.GET or None)

    if request.method == 'GET':
        objects = worker_filter(objects, form)
    
    paginator = Paginator(objects, 12)
    page_number = request.GET.get('page')
    worker_page = paginator.get_page(page_number)

    # depending of the user type write one title or another
    persons_dict = [user for user in worker_page]
    for person in persons_dict:
        person.pop('_state', None)
        # remove null values
        for key, value in list(person.items()):
            if value is None or value == '':
                person[key] = '-'
    
    persons_json = json.dumps(persons_dict, cls=CustomJSONEncoder)

    context = {
        'objects': worker_page,
        'object_name': 'trabajador',
        'object_name_en': 'worker',
        'page_title': 'SarandONGa 💃 - Gestión de Trabajadores',
        'title': title,
        'objects_json': persons_json,
        'form': form
    }

    return render(request, 'person/users/list.html', context)


def worker_filter(queryset, form):

    qsearch = form['qsearch'].value()
    birth_date_min = form['birth_date_min'].value()
    birth_date_max = form['birth_date_max'].value()
    sex = form['sex'].value()

    if qsearch is not None:
        if qsearch.strip() != '':
            queryset = queryset.filter(
                Q(email__icontains=qsearch) |
                Q(name__icontains=qsearch) |
                Q(surname__icontains=qsearch) |
                Q(address__icontains=qsearch) |
                Q(city__icontains=qsearch) |
                Q(telephone__icontains=qsearch) |
                Q(postal_code__icontains=qsearch)
            )

    if is_valid_queryparam(birth_date_min):
        queryset = queryset.filter(birth_date__gte=birth_date_min)

    if is_valid_queryparam(birth_date_max):
        queryset = queryset.filter(birth_date__lte=birth_date_max)

    if is_valid_queryparam(sex):
        queryset = queryset.filter(sex=sex)

    return queryset


@login_required
def worker_details(request, worker_id): 
    worker = get_object_or_404(Worker, id=worker_id)
    if worker.ong == request.user.ong:
        fields = [f for f in Worker._meta.get_fields() if f.name not in ['id', 'photo', 'password', 'user_type',
                                                                         'name', 'surname', 'service', 'ong', 'person_ptr', 'logentry', 'last_login', 'is_active', 'is_admin']]

        info = [getattr(worker, f.name) for f in fields]

        fields_info = dict(zip([f.verbose_name for f in fields], info))

        items = list(fields_info.items())

        for item in items:
            if ((item[1] == True or item[1] == 'True') and type(item[1]) != int):
                items[items.index(item)] = (item[0], 'Sí')
            elif ((item[1] == False or item[1] == 'False') and type(item[1]) != int):
                items[items.index(item)] = (item[0], 'No')
            elif (item[0] == 'Género' and item[1] != None):
                choices = Worker._meta.get_field('sex').choices
                value = [choice[1]
                         for choice in choices if choice[0] == item[1]][0]
                items[items.index(item)] = (item[0], value)

        items = [item for item in items if item[1] !=
                 None and item[1] != '' and item[1] != []]

        mid = math.ceil(len(items) / 2)
        if worker.name:
            page_title = 'SarandONGa 💃 - ' + worker.name + ' ' + worker.surname
        else:
            page_title = 'SarandONGa 💃 - Trabajador'
        
        context = {'worker': worker, 'info_left': items[:mid], 'info_right': items[mid:], 'page_title': page_title}

        return render(request, 'person/users/details.html', context)
    else:
        return custom_403(request)


@login_required
def worker_delete(request, worker_id):
    worker = get_object_or_404(Worker, id=worker_id)
    if worker.ong == request.user.ong:
        worker.delete()
        return redirect('worker_list')
    else:
        return custom_403(request)


@login_required
@videssur_required
def child_list(request):
    objects = Child.objects.filter(ong=request.user.ong).values()

    title = "Gestión de Niños"
    form = FilterChildForm(request.GET or None)

    if request.method == "GET":
        objects = child_filter(objects, form)

    paginator = Paginator(objects, 12)
    page_number = request.GET.get('page')
    child_page = paginator.get_page(page_number)

    # depending of the user type write one title or another
    persons_dict = [child for child in child_page]
    for person in persons_dict:
        person.pop('_state', None)
        # remove null values
        for key, value in list(person.items()):
            if value is None or value == '':
                person[key] = '-'

    persons_json = json.dumps(persons_dict, cls=CustomJSONEncoder)

    context = {
        'objects': child_page,
        'object_name': 'niño',
        'object_name_en': 'child',
        'title': title,
        'page_title': 'SarandONGa 💃 - Gestión de Niños',
        'objects_json': persons_json,
        'form': form,
    }

    return render(request, 'person/users/list.html', context)


def child_filter(queryset, form):

    qsearch = form['qsearch'].value()
    birth_date_min = form['birth_date_min'].value()
    birth_date_max = form['birth_date_max'].value()
    sex = form['sex'].value()
    is_older = form['is_older'].value()
    is_sponsored = form['is_sponsored'].value()

    if qsearch is not None:
        if qsearch.strip() != '':
            queryset = queryset.filter(
                Q(name__icontains=qsearch) |
                Q(surname__icontains=qsearch) |
                Q(email__icontains=qsearch) |
                Q(city__icontains=qsearch) |
                Q(address__icontains=qsearch) |
                Q(telephone__icontains=qsearch) |
                Q(postal_code__icontains=qsearch) |
                Q(expected_mission_time__icontains=qsearch) |
                Q(mission_house__icontains=qsearch) |
                Q(site__icontains=qsearch) |
                Q(subsite__icontains=qsearch) |
                Q(father_name__icontains=qsearch) |
                Q(father_profession__icontains=qsearch) |
                Q(mother_name__icontains=qsearch) |
                Q(mother_profession__icontains=qsearch)
            )

    if is_valid_queryparam(birth_date_min):
        queryset = queryset.filter(birth_date__gte=birth_date_min)

    if is_valid_queryparam(birth_date_max):
        queryset = queryset.filter(birth_date__lte=birth_date_max)

    if is_valid_queryparam(sex):
        queryset = queryset.filter(sex=sex)

    if is_valid_queryparam(is_older):
        if is_older == 'S':
            queryset = queryset.filter(
                birth_date__lte=date.today() - relativedelta(years=18))
        elif is_older == 'N':
            queryset = queryset.filter(
                birth_date__gt=date.today() - relativedelta(years=18))

    if is_valid_queryparam(is_sponsored):

        sponshorships = Sponsorship.objects.all()
        sponsored_children = set()

        for sponsorship in sponshorships:
            if sponsorship.termination_date is None:
                sponsored_children.add(sponsorship.child.id)
            elif sponsorship.termination_date > date.today():
                sponsored_children.add(sponsorship.child.id)

        if is_sponsored == 'S':
            queryset = queryset.filter(id__in=sponsored_children)
        elif is_sponsored == 'N':
            queryset = queryset.exclude(id__in=sponsored_children)

    return queryset


@login_required
@asem_required
def user_list(request):
    objects = ASEMUser.objects.filter(ong=request.user.ong).values()

    form = FilterAsemUserForm(request.GET or None)
    objects = asemuser_filter(objects, form)

    if request.method == 'POST':
        try:
            response = HttpResponse()
            response['Content-Disposition'] = 'attachment; filename=asem_users.xlsx'
            writer = csv.writer(response)
            writer.writerow(['id', 'email', 'nombre', 'apellido', 'fecha_nacimiento', 'sexo', 'ciudad', 'direccion', 'telefono', 'codigo_postal', 'foto', 'tipo_usuario',
                            'es_miembro', 'condicion', 'tipo_correspondencia', 'estado', 'tamaño_unidad_familiar', 'casa_propia', 'vehiculo_propio', 'numero_cuenta_bancaria', 'ong'])
            asemUser_fields = objects.values_list('id', 'email', 'name', 'surname', 'birth_date', 'sex', 'city', 'address', 'telephone', 'postal_code', 'photo', 'user_type', 'member', 'condition', 'correspondence', 'status', 'family_unit_size', 'own_home', 'own_vehicle', 'bank_account_number', 'ong')
            for a in asemUser_fields:
                writer.writerow(a)
            message = ("Exportado correctamente")
            messages.success(request, message)
            return response
        except ValidationErr:
            message = ("Error in exporting data. There are null data in rows")
            messages.error(request, message)
            return render(request, 'person/users/list.html')

    paginator = Paginator(objects, 12)
    page_number = request.GET.get('page')
    user_page = paginator.get_page(page_number)

    title = "Gestión de Usuarios ASEM"

    # depending of the user type write one title or another
    persons_dict = [user for user in user_page]
    for person in persons_dict:
        person.pop('_state', None)
        # remove null values
        for key, value in list(person.items()):
            if value is None or value == '':
                person[key] = '-'

    persons_json = json.dumps(persons_dict, cls=CustomJSONEncoder)

    context = {
        'objects': user_page,
        'object_name': 'usuario',
        'object_name_en': 'user',
        'title': title,
        'page_title': 'SarandONGa 💃 - Gestión de Usuarios ASEM',
        'objects_json': persons_json,
        'form': form,
    }

    return render(request, 'person/users/list.html', context)


def is_valid_queryparam(param):
    return param != '' and param is not None


def asemuser_filter(queryset, form):

    q = form['qsearch'].value()
    birth_date_min = form['birth_date_min'].value()
    birth_date_max = form['birth_date_max'].value()
    sex = form['sex'].value()
    condition = form['condition'].value()
    member = form['member'].value()
    user_type = form['user_type'].value()
    status = form['status'].value()

    if q is not None:
        if q.strip() != '':
            queryset = queryset.filter(
                Q(name__icontains=q) |
                Q(surname__icontains=q) |
                Q(address__icontains=q) |
                Q(city__icontains=q) |
                Q(postal_code__icontains=q) |
                Q(email__icontains=q) |
                Q(telephone__icontains=q) |
                Q(bank_account_number__icontains=q)
            )

    if is_valid_queryparam(birth_date_min):
        queryset = queryset.filter(birth_date__gte=birth_date_min)

    if is_valid_queryparam(birth_date_max):
        queryset = queryset.filter(birth_date__lte=birth_date_max)

    if is_valid_queryparam(sex):
        queryset = queryset.filter(sex=sex)

    if is_valid_queryparam(condition):
        queryset = queryset.filter(condition=condition)

    if is_valid_queryparam(member):
        queryset = queryset.filter(member=member)

    if is_valid_queryparam(user_type):
        queryset = queryset.filter(user_type=user_type)
        
    if is_valid_queryparam(status):
        queryset = queryset.filter(status=status)

    return queryset


@login_required
@videssur_required
def godfather_create(request):
    form = CreateNewGodFather(initial={'ong': request.user.ong})
    if request.method == 'POST':
        form = CreateNewGodFather(request.POST, request.FILES)
        if form.is_valid():
            try:
                ong = request.user.ong
                godfather = form.save(commit=False)
                godfather.ong = ong
                godfather.save()
                return redirect('godfather_list')
            except ValidationErr as v:
                messages.error(request, str(v.args[0]))
        else:
            messages.error(request, 'Formulario con errores')

    context = {
        'form': form, 
        'title': 'Añadir Padrino', 
        'page_title': 'SarandONGa 💃 - Añadir Padrino'
        }

    return render(request, 'person/godfather/register.html', context)


@login_required
@videssur_required
def godfather_update(request, godfather_id):
    godfather = get_object_or_404(GodFather, id=godfather_id)
    form = CreateNewGodFather(instance=godfather)
    if request.user.ong == godfather.ong:
        if request.method == 'POST':
            form = CreateNewGodFather(
                request.POST or None, request.FILES or None, instance=godfather)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('godfather_list')
                except ValidationErr as v:
                    messages.error(request, str(v.args[0]))
            else:
                messages.error(request, 'Formulario con errores')
    else:
        return custom_403(request)
    
    context = {
        'form': form, 
        'title': "Editar Padrino", 
        'page_title': 'SarandONGa 💃 - Editar Padrino'
        }
    
    return render(request, 'person/godfather/register.html', context)


@login_required
@videssur_required
def godfather_details(request, godfather_id):
    godfather = get_object_or_404(GodFather, id=godfather_id)

    fields = [f for f in GodFather._meta.get_fields() if f.name not in ['id', 'photo', 'password',
                                                                        'user_type', 'name', 'surname', 'payment', 'sponsorship', 'person_ptr', 'ong']]

    info = [getattr(godfather, f.name) for f in fields]

    fields_info = dict(zip([f.verbose_name for f in fields], info))

    items = list(fields_info.items())

    for item in items:
        if ((item[1] == True or item[1] == 'True') and type(item[1]) != int):
            items[items.index(item)] = (item[0], 'Sí')
        elif ((item[1] == False or item[1] == 'False') and type(item[1]) != int):
            items[items.index(item)] = (item[0], 'No')
        elif (item[0] == 'Género' and item[1] != None):
            choices = GodFather._meta.get_field('sex').choices
            value = [choice[1]
                     for choice in choices if choice[0] == item[1]][0]
            items[items.index(item)] = (item[0], value)
        elif (item[0] == 'Método de pago'):
            choices = GodFather._meta.get_field('payment_method').choices
            value = [choice[1]
                     for choice in choices if choice[0] == item[1]][0]
            items[items.index(item)] = (item[0], value)
        elif (item[0] == 'Cantidad'):
            items[items.index(item)] = (item[0], str(item[1]) + '€')
        elif (item[0] == 'Frecuencia de pago'):
            choices = GodFather._meta.get_field('frequency').choices
            value = [choice[1]
                     for choice in choices if choice[0] == item[1]][0]
            items[items.index(item)] = (item[0], value)
        elif (item[0] == 'Estado'):
            choices = GodFather._meta.get_field('status').choices
            value = [choice[1]
                     for choice in choices if choice[0] == item[1]][0]
            items[items.index(item)] = (item[0], value)

    sponsorships = Sponsorship.objects.filter(godfather=godfather)
    if sponsorships:
        children = [sponsorship.child for sponsorship in sponsorships if sponsorship.termination_date ==
                    None or sponsorship.termination_date > datetime.date(datetime.now())]
        items.append(('Niños apadrinados', children))

    items = [item for item in items if item[1] != None and item[1] != '' and item[1] != []]

    mid = math.ceil(len(items) / 2)

    page_title = 'SarandONGa 💃 - ' + godfather.name + ' ' + godfather.surname
    
    context = {
        'godfather': godfather, 
        'info_left': items[:mid], 
        'info_right': items[mid:], 
        'page_title': page_title
        }

    return render(request, 'person/users/details.html', context)


@login_required
@videssur_required
def godfather_delete(request, godfather_id):
    godfather = get_object_or_404(GodFather, id=godfather_id)
    godfather.delete()
    return redirect('godfather_list')


@login_required
@videssur_required
def child_create(request):
    form = CreateNewChild(initial={'ong': request.user.ong})
    if request.method == 'POST':
        form = CreateNewChild(request.POST, request.FILES)
        if form.is_valid():
            ong = request.user.ong  # it is videssur basically
            child = form.save(commit=False)
            child.ong = ong
            child.save()
            return redirect('child_list')
        else:
            messages.error(request, 'Formulario con errores')
    
    context = {
        'form': form, 
        'title': 'Añadir Niño', 
        'page_title': 'SarandONGa 💃 - Añadir Niño'
        }
            
    return render(request, 'person/child/register.html', context)


@login_required
@videssur_required
def child_update(request, child_id):
    child = get_object_or_404(Child, id=child_id)
    if request.user.ong == child.ong:
        form = CreateNewChild(instance=child)
        if request.method == 'POST':
            form = CreateNewChild(request.POST or None,
                                  request.FILES or None, instance=child)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('child_list')
                except ValidationErr as v:
                    messages.error(request, str(v.args[0]))
            else:
                messages.error(request, 'Formulario con errores')
    else:
        return custom_403(request)

    context = {
        'form': form, 
        'title': "Editar Niño", 
        'page_title': 'SarandONGa 💃 - Editar Niño'
        }

    return render(request, 'person/child/register.html', context)


@login_required
@videssur_required
def child_details(request, child_id):
    child = get_object_or_404(Child, id=child_id)
    fields = [f for f in Child._meta.get_fields() if f.name not in ['id', 'photo', 'password',
                                                                    'user_type', 'name', 'surname', 'service', 'ong', 'person_ptr', 'sponsorship']]

    info = [getattr(child, f.name) for f in fields]

    fields_info = dict(zip([f.verbose_name for f in fields], info))

    items = list(fields_info.items())

    for item in items:
        if ((item[1] == True or item[1] == 'True') and type(item[1]) != int):
            items[items.index(item)] = (item[0], 'Sí')
        elif ((item[1] == False or item[1] == 'False') and type(item[1]) != int):
            items[items.index(item)] = (item[0], 'No')
        elif (item[0] == 'Género' and item[1] != None):
            choices = Child._meta.get_field('sex').choices
            value = [choice[1]
                     for choice in choices if choice[0] == item[1]][0]
            items[items.index(item)] = (item[0], value)
        elif (item[0] == 'Tipo de correspondencia'):
            choices = Child._meta.get_field('correspondence').choices
            value = [choice[1]
                     for choice in choices if choice[0] == item[1]][0]
            items[items.index(item)] = (item[0], value)

    sponsorships = Sponsorship.objects.filter(child=child)
    if sponsorships:
        godfathers = [sponsorship.godfather.all() for sponsorship in sponsorships if sponsorship.termination_date ==
                      None or sponsorship.termination_date > datetime.date(datetime.now())]
        godfathers = [g for godfather in godfathers for g in godfather]
        items.append(('Padrinos', godfathers))

    items = [item for item in items if item[1] !=
             None and item[1] != '' and item[1] != []]

    items = [item for item in items if item[1] != None and item[1] != '' and item[1] != []]

    mid = math.ceil(len(items) / 2)

    page_title = 'SarandONGa 💃 - ' + child.name + ' ' + child.surname
    
    context = {
        'child': child, 
        'info_left': items[:mid], 
        'info_right': items[mid:], 
        'page_title': page_title
        }
    
    return render(request, 'person/users/details.html', context)


@login_required
@videssur_required
def child_delete(request, child_id):
    child = get_object_or_404(Child, id=child_id)
    child.delete()
    return redirect('child_list')


@login_required
def volunteer_list(request):
    objects = Volunteer.objects.filter(ong=request.user.ong).values()

    form = FilterVolunteerForm(request.GET or None)
    if request.method == 'GET':
        objects = volunteer_filter(objects, form)
    
    paginator = Paginator(objects, 12)
    page_number = request.GET.get('page')
    user_page = paginator.get_page(page_number)

    page_title = 'SarandONGa 💃 - Gestión de Voluntarios'
    
    # depending of the user type write one title or another
    persons_dict = [user for user in user_page]
    for person in persons_dict:
        person.pop('_state', None)
        # remove null values
        for key, value in list(person.items()):
            if value is None or value == '':
                person[key] = '-'

    persons_json = json.dumps(persons_dict, cls=CustomJSONEncoder)

    query_str = "&qsearch="
    keys = request.GET.keys()

    if "qsearch" in keys:
        query_str += request.GET["qsearch"]
    
    query_str += "&birth_date_min="
    if "birth_date_min" in keys:
        query_str += request.GET["birth_date_min"]

    query_str += "&birth_date_max="
    if "birth_date_max" in keys:
        query_str += request.GET["birth_date_max"]

    query_str += "&sex="
    if "sex" in keys:
        query_str += request.GET["sex"]

    query_str += "&volunteer_type="
    if "volunteer_type" in keys:
        query_str += request.GET["volunteer_type"]

    query_str += "&min_dedication_time="
    if "min_dedication_time" in keys:
        query_str += request.GET["min_dedication_time"]

    query_str += "&max_dedication_time="
    if "max_dedication_time" in keys:
        query_str += request.GET["max_dedication_time"]

    query_str += "&min_contract_start="
    if "min_contract_start" in keys:
        query_str += request.GET["min_contract_start"]

    query_str += "&max_contract_start="
    if "max_contract_start" in keys:
        query_str += request.GET["max_contract_start"]

    query_str += "&min_contract_end="
    if "min_contract_end" in keys:
        query_str += request.GET["min_contract_end"]

    query_str += "&max_contract_end="
    if "max_contract_end" in keys:
        query_str += request.GET["max_contract_end"]

    query_str += "&raffle="
    if "raffle" in keys:
        query_str += request.GET["raffle"]

    query_str += "&lottery="
    if "lottery" in keys:
        query_str += request.GET["lottery"]

    query_str += "&is_member="
    if "is_member" in keys:
        query_str += request.GET["is_member"]

    query_str += "&pres_table="
    if "pres_table" in keys:
        query_str += request.GET["pres_table"]

    query_str += "&is_contributor="
    if "is_contributor" in keys:
        query_str += request.GET["is_contributor"]

    context = {
        'objects': user_page,
        'object_name': 'voluntario',
        'object_name_en': 'volunteer',
        'page_title': page_title,
        'title': 'Gestión de Voluntarios',
        'objects_json': persons_json,
        'search_text': 'Buscar voluntario...',
        'form' : form,
        'query_str': query_str
    }

    return render(request, 'person/users/list.html', context)


def volunteer_filter(queryset, form):

    q = form['qsearch'].value()
    birth_date_min = form['birth_date_min'].value()
    birth_date_max = form['birth_date_max'].value()
    sex = form['sex'].value()
    volunteer_type = form['volunteer_type'].value()

    if q is not None:
        if q.strip() != "":
            queryset = queryset.filter(
                Q(name__icontains=q) |
                Q(surname__icontains=q) |
                Q(address__icontains=q) |
                Q(city__icontains=q) |
                Q(postal_code__icontains=q) |
                Q(email__icontains=q) |
                Q(telephone__icontains=q) |
                Q(birth_date__icontains=q) |
                Q(sex__icontains=q) |
                Q(dni__icontains=q) |
                Q(job__icontains=q) |
                Q(dedication_time__icontains=q) |
                Q(contract_start_date__icontains=q) |
                Q(contract_end_date__icontains=q) |
                Q(notes__icontains=q) |
                Q(entity__icontains=q) |
                Q(table__icontains=q) |
                Q(volunteer_type__icontains=q)
            )

    if is_valid_queryparam(birth_date_min):
        queryset = queryset.filter(birth_date__gte=birth_date_min)

    if is_valid_queryparam(birth_date_max):
        queryset = queryset.filter(birth_date__lte=birth_date_max)

    if is_valid_queryparam(sex):
        queryset = queryset.filter(sex=sex)

    if is_valid_queryparam(volunteer_type):
        queryset = queryset.filter(volunteer_type=volunteer_type)

    return queryset


@login_required
def volunteer_details(request, volunteer_id):
    volunteer = get_object_or_404(Volunteer, id=volunteer_id)
    this_ong = request.user.ong
    if volunteer.ong == this_ong:
        fields = []
        
        if str(this_ong).lower() == "asem":
            fields = [f for f in Volunteer._meta.get_fields() if f.name not in [
            'id', 'photo', 'password', 'user_type', 'name', 'surname',
            'service', 'ong', 'person_ptr']]
        elif str(this_ong).lower() == "videssur":
            fields = [f for f in Volunteer._meta.get_fields() if f.name not in [
            'id', 'photo', 'password', 'user_type', 'name', 'surname',
            'service', 'ong', 'person_ptr','raffle','lottery','is_member',
            'pres_table','is_contributor','entity','table']]

        info = [getattr(volunteer, f.name) for f in fields]

        fields_info = dict(zip([f.verbose_name for f in fields], info))

        items = list(fields_info.items())

        for item in items:
            if ((item[1] == True or item[1] == 'True') and type(item[1]) != int):
                items[items.index(item)] = (item[0], 'Sí')
            elif ((item[1] == False or item[1] == 'False') and type(item[1]) != int):
                items[items.index(item)] = (item[0], 'No')
            elif (item[0] == 'Género' and item[1] != None):
                choices = Volunteer._meta.get_field('sex').choices
                value = [choice[1]
                         for choice in choices if choice[0] == item[1]][0]
                items[items.index(item)] = (item[0], value)
            elif (item[0] == 'Tiempo de dedicación'):
                items[items.index(item)] = (item[0], str(item[1]) + ' horas')
            elif (item[0] == 'Tipo de voluntario'):
                choices = Volunteer._meta.get_field('volunteer_type').choices
                value = [choice[1]
                         for choice in choices if choice[0] == item[1]][0]
                items[items.index(item)] = (item[0], value)

        items = [item for item in items if item[1] !=
                 None and item[1] != '' and item[1] != []]

        mid = math.ceil(len(items) / 2)

        page_title = 'SarandONGa 💃 - ' + volunteer.name + ' ' + volunteer.surname
        
        context = {
            'volunteer': volunteer, 
            'info_left': items[:mid], 
            'info_right': items[mid:], 
            'page_title': page_title
            }
        
        return render(request, 'person/users/details.html', context)
    else:
        return custom_403(request)


@login_required
def volunteer_create(request):
    form = CreateNewVolunteer(initial={'ong': request.user.ong})
    if request.method == 'POST':
        form = CreateNewVolunteer(request.POST, request.FILES)
        if form.is_valid():
            ong = request.user.ong
            # if the user is anonymous, the ong is not set yet. Actually, it won't be possible to create a volunteer unless the user is logged in
            volunteer = form.save(commit=False)
            volunteer.ong = ong
            volunteer.save()
            return redirect('volunteer_list')
        else:
            messages.error(request, 'Formulario con errores')

    context = {
        'form': form, 
        'title': 'Añadir Voluntario', 
        'page_title': 'SarandONGa 💃 - Añadir Voluntario'
        }

    return render(request, 'person/volunteers/register.html', context)


@login_required
def volunteer_delete(request, volunteer_id):
    volunteer = Volunteer.objects.get(id=volunteer_id)
    if volunteer.ong == request.user.ong:
        volunteer.delete()
        return redirect('volunteer_list')
    else:
        return custom_403(request)


@login_required
def volunteer_update(request, volunteer_id):
    volunteer = get_object_or_404(Volunteer, id=volunteer_id)
    if volunteer.ong == request.user.ong:
        form = CreateNewVolunteer(instance=volunteer)
        if request.method == 'POST':
            form = CreateNewVolunteer(
                request.POST, request.FILES, instance=volunteer)

            if form.is_valid():
                form.save()
                return redirect('volunteer_list')
            else:
                messages.error(request, 'Formulario con errores')
    else:
        return custom_403(request)
    
    context = {
        'form': form, 
        'title': 'Editar Voluntario', 
        'page_title': 'SarandONGa 💃 - Editar Voluntario'
        }
    
    return render(request, 'person/volunteers/register.html', context)


def child_age(request):
    childs = Child.objects.values('name', 'birth_date')
    return JsonResponse(list(childs), safe=False)

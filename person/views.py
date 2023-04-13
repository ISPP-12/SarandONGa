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
    title = "Gestión de Padrinos"

    form = FilterGodfatherForm(request.GET or None)
    objects = godfather_filter(objects, form)

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
        'form': form,
    }

    return render(request, 'users/list.html', context)


def godfather_filter(queryset, form):

    q = form['qsearch'].value()
    min_birth_date = form['min_birth_date'].value()
    max_birth_date = form['max_birth_date'].value()
    sex = form['sex'].value()
    payment_method = form['payment_method'].value()
    frequency = form['frequency'].value()
    min_amount = form['min_amount'].value()
    max_amount = form['max_amount'].value()
    min_start_date = form['min_start_date'].value()
    max_start_date = form['max_start_date'].value()
    min_end_date = form['min_end_date'].value()
    max_end_date = form['max_end_date'].value()
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

    if is_valid_queryparam(min_birth_date):
        queryset = queryset.filter(birth_date__gte=min_birth_date)

    if is_valid_queryparam(max_birth_date):
        queryset = queryset.filter(birth_date__lte=max_birth_date)

    if is_valid_queryparam(sex):
        queryset = queryset.filter(sex=sex)

    if is_valid_queryparam(payment_method):
        queryset = queryset.filter(payment_method=payment_method)

    if is_valid_queryparam(min_amount):
        queryset = queryset.filter(amount__gte=min_amount)

    if is_valid_queryparam(max_amount):
        queryset = queryset.filter(amount__lte=max_amount)

    if is_valid_queryparam(min_start_date):
        queryset = queryset.filter(start_date__gte=min_start_date)

    if is_valid_queryparam(max_start_date):
        queryset = queryset.filter(start_date__lte=max_start_date)

    if is_valid_queryparam(min_end_date):
        queryset = queryset.filter(termination_date__gte=min_end_date)

    if is_valid_queryparam(max_end_date):
        queryset = queryset.filter(termination_date__lte=max_end_date)

    if is_valid_queryparam(status):
        queryset = queryset.filter(status=status)

    if is_valid_queryparam(frequency):
        queryset = queryset.filter(frequency=frequency)

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

    return render(request, 'asem_user/asem_user_form.html', {'form': form, 'title': 'Añadir Usuario ASEM'})


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
    return render(request, 'asem_user/asem_user_form.html', {'form': form})


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

    context = {'asem_user': asem_user,
               'info_left': items[:mid], 'info_right': items[mid:]}

    return render(request, 'users/details.html', context)


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

    return render(request, 'workers/register.html', {'form': form, 'title': 'Añadir trabajador'})


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
        context = {'form': form, 'title': 'Actualizar Trabajador'}
    else:
        return custom_403(request)
    return render(request, 'workers/register.html', context)


@login_required
def worker_list(request):
    objects = Worker.objects.filter(ong=request.user.ong).values()
    title = 'Gestión de Trabajadores'
    form = FilterWorkerForm(request.GET or None)

    if request.method == 'GET':
        objects = worker_filter(objects, form)

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
        'form': form
    }

    return render(request, 'users/list.html', context)


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

        context = {'worker': worker,
                   'info_left': items[:mid], 'info_right': items[mid:]}

        return render(request, 'users/details.html', context)
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
    for d in persons_dict:
        d.pop('_state', None)

    persons_json = json.dumps(persons_dict, cls=CustomJSONEncoder)

    context = {
        'objects': child_page,
        'object_name': 'niño',
        'object_name_en': 'child',
        'title': title,
        'objects_json': persons_json,
        'form': form,
    }

    return render(request, 'users/list.html', context)


def child_filter(queryset, form):

    qsearch = form['qsearch'].value()
    birth_date_min = form['birth_date_min'].value()
    birth_date_max = form['birth_date_max'].value()
    sex = form['sex'].value()
    start_date_min = form['start_date_min'].value()
    start_date_max = form['start_date_max'].value()
    termination_date_min = form['termination_date_min'].value()
    termination_date_max = form['termination_date_max'].value()
    number_brothers_siblings = form['number_brothers_siblings'].value()
    correspondence = form['correspondence'].value()
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

    if is_valid_queryparam(start_date_min):
        queryset = queryset.filter(start_date__gte=start_date_min)

    if is_valid_queryparam(start_date_max):
        queryset = queryset.filter(start_date__lte=start_date_max)

    if is_valid_queryparam(termination_date_min):
        queryset = queryset.filter(termination_date__gte=termination_date_min)

    if is_valid_queryparam(termination_date_max):
        queryset = queryset.filter(termination_date__lte=termination_date_max)

    if is_valid_queryparam(number_brothers_siblings):
        queryset = queryset.filter(
            number_brothers_siblings=number_brothers_siblings)

    if is_valid_queryparam(correspondence):
        queryset = queryset.filter(correspondence=correspondence)

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
            asemUser_fields = objects.values_list('id', 'email', 'name', 'surname', 'birth_date', 'sex', 'city', 'address', 'telephone', 'postal_code', 'photo',
                                                  'user_type', 'member', 'condition', 'correspondence', 'status', 'family_unit_size', 'own_home', 'own_vehicle', 'bank_account_number', 'ong')
            for a in asemUser_fields:
                writer.writerow(a)
            message = ("Exportado correctamente")
            messages.success(request, message)
            return response
        except ValidationErr:
            message = ("Error in exporting data. There are null data in rows")
            messages.error(request, message)
            return render(request, 'users/list.html')

    paginator = Paginator(objects, 12)
    page_number = request.GET.get('page')
    user_page = paginator.get_page(page_number)

    title = "Gestión de Usuarios ASEM"

    # depending of the user type write one title or another
    persons_dict = [user for user in user_page]
    for d in persons_dict:
        d.pop('_state', None)

    persons_json = json.dumps(persons_dict, cls=CustomJSONEncoder)

    context = {
        'objects': user_page,
        'object_name': 'usuario',
        'object_name_en': 'user',
        'title': title,
        'objects_json': persons_json,
        'form': form,
    }

    return render(request, 'users/list.html', context)


def is_valid_queryparam(param):
    return param != '' and param is not None


def asemuser_filter(queryset, form):

    q = form['qsearch'].value()
    min_date = form['min_date'].value()
    max_date = form['max_date'].value()
    sex = form['sex'].value()
    condition = form['condition'].value()
    member = form['member'].value()
    user_type = form['user_type'].value()
    correspondence = form['correspondence'].value()
    status = form['status'].value()
    fam_size_min = form['fam_size_min'].value()
    fam_size_max = form['fam_size_max'].value()
    own_home = form['own_home'].value()
    own_vehicle = form['own_vehicle'].value()

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

    if is_valid_queryparam(min_date):
        queryset = queryset.filter(birth_date__gte=min_date)

    if is_valid_queryparam(max_date):
        queryset = queryset.filter(birth_date__lte=max_date)

    if is_valid_queryparam(sex):
        queryset = queryset.filter(sex=sex)

    if is_valid_queryparam(condition):
        queryset = queryset.filter(condition=condition)

    if is_valid_queryparam(member):
        queryset = queryset.filter(member=member)

    if is_valid_queryparam(user_type):
        queryset = queryset.filter(user_type=user_type)

    if is_valid_queryparam(correspondence):
        queryset = queryset.filter(correspondence=correspondence)

    if is_valid_queryparam(status):
        queryset = queryset.filter(status=status)

    if is_valid_queryparam(fam_size_min):
        queryset = queryset.filter(family_unit_size__gte=fam_size_min)

    if is_valid_queryparam(fam_size_max):
        queryset = queryset.filter(family_unit_size__lte=fam_size_max)

    if is_valid_queryparam(own_home):
        queryset = queryset.filter(own_home=own_home)

    if is_valid_queryparam(own_vehicle):
        queryset = queryset.filter(own_vehicle=own_vehicle)

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

    return render(request, 'person/godfather/form.html', {'form': form, 'title': 'Añadir Padrino'})


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
    return render(request, 'person/godfather/form.html', {'form': form})


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

    items = [item for item in items if item[1] !=
             None and item[1] != '' and item[1] != []]

    mid = math.ceil(len(items) / 2)

    context = {'godfather': godfather,
               'info_left': items[:mid], 'info_right': items[mid:]}

    return render(request, 'users/details.html', context)


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
    return render(request, 'person/child/create_child.html', {'form': form, 'title': 'Añadir Niño'})


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

    return render(request, 'person/child/create_child.html', {'form': form})


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

    mid = math.ceil(len(items) / 2)

    context = {'child': child,
               'info_left': items[:mid], 'info_right': items[mid:]}
    return render(request, 'users/details.html', context)


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
    objects = volunteer_filter(objects, form)

    paginator = Paginator(objects, 12)
    page_number = request.GET.get('page')
    user_page = paginator.get_page(page_number)

    title = 'Gestión de Voluntarios'
    # depending of the user type write one title or another
    persons_dict = [user for user in user_page]
    for d in persons_dict:
        d.pop('_state', None)

    persons_json = json.dumps(persons_dict, cls=CustomJSONEncoder)

    context = {
        'objects': user_page,
        'object_name': 'voluntario',
        'object_name_en': 'volunteer',
        'title': title,
        'objects_json': persons_json,
        'search_text': 'Buscar voluntario...',
        'form': form,
    }

    return render(request, 'users/list.html', context)


def volunteer_filter(queryset, form):

    q = form['qsearch'].value()
    min_birth_date = form['min_birth_date'].value()
    max_birth_date = form['max_birth_date'].value()
    sex = form['sex'].value()
    volunteer_type = form['volunteer_type'].value()
    min_dedication_time = form['min_dedication_time'].value()
    max_dedication_time = form['max_dedication_time'].value()
    min_contract_start = form['min_contract_start'].value()
    max_contract_start = form['max_contract_start'].value()
    min_contract_end = form['min_contract_end'].value()
    max_contract_end = form['max_contract_end'].value()
    raffle = form['raffle'].value()
    lottery = form['lottery'].value()
    is_member = form['is_member'].value()
    pres_table = form['pres_table'].value()
    is_contributor = form['is_contributor'].value()

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

    if is_valid_queryparam(min_birth_date):
        queryset = queryset.filter(birth_date__gte=min_birth_date)

    if is_valid_queryparam(max_birth_date):
        queryset = queryset.filter(birth_date__lte=max_birth_date)

    if is_valid_queryparam(sex):
        queryset = queryset.filter(sex=sex)

    if is_valid_queryparam(volunteer_type):
        queryset = queryset.filter(volunteer_type=volunteer_type)

    if is_valid_queryparam(min_dedication_time):
        queryset = queryset.filter(dedication_time__gte=min_dedication_time)

    if is_valid_queryparam(max_dedication_time):
        queryset = queryset.filter(dedication_time__lte=max_dedication_time)

    if is_valid_queryparam(min_contract_start):
        queryset = queryset.filter(contract_start_date__gte=min_contract_start)

    if is_valid_queryparam(max_contract_start):
        queryset = queryset.filter(contract_start_date__lte=max_contract_start)

    if is_valid_queryparam(min_contract_end):
        queryset = queryset.filter(contract_end_date__gte=min_contract_end)

    if is_valid_queryparam(max_contract_end):
        queryset = queryset.filter(contract_end_date__lte=max_contract_end)

    if is_valid_queryparam(raffle):
        queryset = queryset.filter(raffle=raffle)

    if is_valid_queryparam(lottery):
        queryset = queryset.filter(lottery=lottery)

    if is_valid_queryparam(is_member):
        queryset = queryset.filter(is_member=is_member)

    if is_valid_queryparam(pres_table):
        queryset = queryset.filter(pres_table=pres_table)

    if is_valid_queryparam(is_contributor):
        queryset = queryset.filter(is_contributor=is_contributor)

    return queryset


@login_required
def volunteer_details(request, volunteer_id):
    volunteer = get_object_or_404(Volunteer, id=volunteer_id)
    if volunteer.ong == request.user.ong:
        fields = [f for f in Volunteer._meta.get_fields() if f.name not in [
            'id', 'photo', 'password', 'user_type', 'name', 'surname', 'service', 'ong', 'person_ptr']]

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

        context = {'volunteer': volunteer,
                   'info_left': items[:mid], 'info_right': items[mid:]}

        return render(request, 'users/details.html', context)
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
    return render(request, 'volunteers/volunteers_form.html', {'form': form, 'title': 'Añadir Voluntario'})


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
    return render(request, 'volunteers/volunteers_form.html', {'form': form})


def child_age(request):
    ninos = Child.objects.values('name', 'birth_date')
    return JsonResponse(list(ninos), safe=False)

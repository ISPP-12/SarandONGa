from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import GodFather, ASEMUser, Worker, Child, Volunteer, SEX_TYPES, PAYMENT_METHOD, STATUS, FREQUENCY, CONDITION, MEMBER, ASEMUSER_TYPE, CORRESPONDENCE, HOUSING_TYPE, VOLUNTEER_TYPE
from django.contrib import messages
import json
from datetime import datetime, date
from decimal import Decimal
from main.views import videssur_required, asem_required, custom_403
from .forms import CreateNewGodFather, CreateNewASEMUser, CreateNewVolunteer, CreateNewWorker, CreateNewChild, UpdateWorker, FilterAsemUserForm, FilterWorkerForm
from xml.dom import ValidationErr
from django.core.paginator import Paginator
from django.db.models import Q


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


@login_required
@asem_required
def user_create(request):
    form = CreateNewASEMUser(initial={'ong': request.user.ong})
    if request.method == "POST":
        form = CreateNewASEMUser(request.POST, request.FILES)
        if form.is_valid():
            ong = request.user.ong  # basically, it is ASEM
            user = form.save(commit=False)
            user.ong = ong
            user.save()
            return redirect('user_list')
        else:
            messages.error(request, 'Formulario con errores')

    return render(request, 'asem_user/asem_user_form.html', {"form": form, "title": "Añadir Usuario ASEM"})


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
    if request.method == "POST":
        form = CreateNewASEMUser(
            request.POST, request.FILES, instance=asem_user)
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


@login_required
@asem_required
def asem_user_details(request, asem_user_id):
    asem_user = get_object_or_404(ASEMUser, id=asem_user_id)

    choices_dict = choices_dicts()
    asem_user.condition = choices_dict['condition'][asem_user.condition]
    asem_user.member = choices_dict['member'][asem_user.member]
    asem_user.correspondence = choices_dict['correspondence'][asem_user.correspondence]
    asem_user.user_type = choices_dict['asemuser_type'][asem_user.user_type]
    asem_user.status = choices_dict['status'][asem_user.status]
    asem_user.own_home = choices_dict['housing_type'][asem_user.own_home]

    return render(request, 'users/details.html', {'asem_user': asem_user})


@login_required
def worker_create(request):
    form = CreateNewWorker(initial={'ong': request.user.ong})
    if request.method == "POST":
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

    return render(request, 'workers/register.html', {"form": form, "title": "Añadir trabajador"})


@login_required
def worker_update(request, worker_id):
    worker = get_object_or_404(Worker, id=worker_id)
    if request.user.ong == worker.ong:
        if request.method == "POST":
            form = UpdateWorker(request.POST, request.FILES, instance=worker)
            if form.is_valid():
                form.save()
                return redirect('worker_list')
            else:
                messages.error(request, 'Formulario con errores')

        form = UpdateWorker(instance=worker)
        context = {"form": form, "title": "Actualizar Trabajador"}
    else:
        return custom_403(request)
    return render(request, 'workers/register.html', context)


@login_required
def worker_list(request):
    objects = Worker.objects.filter(ong=request.user.ong).values()
    title = "Gestión de Trabajadores"
    form = FilterWorkerForm(request.GET or None)

    if request.method == "GET":
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

    email = form['email'].value()
    name = form['name'].value()
    surname = form['surname'].value()
    birth_date_min = form['birth_date_min'].value()
    birth_date_max = form['birth_date_max'].value()
    sex = form['sex'].value()
    city = form['city'].value()
    address = form['address'].value()
    telephone = form['telephone'].value()
    postal_code = form['postal_code'].value()

    if email is not None:
        if email.strip() != '':
            queryset = queryset.filter(Q(email__icontains=email))

    if name is not None:
        if name.strip() != '':
            queryset = queryset.filter(Q(name__icontains=name))

    if surname is not None:
        if surname.strip() != '':
            queryset = queryset.filter(Q(surname__icontains=surname))

    if is_valid_queryparam(birth_date_min):
        queryset = queryset.filter(birth_date__gte=birth_date_min)

    if is_valid_queryparam(birth_date_max):
        queryset = queryset.filter(birth_date__lte=birth_date_max)

    if is_valid_queryparam(sex):
        queryset = queryset.filter(sex=sex)

    if city is not None:
        if city.strip() != '':
            queryset = queryset.filter(Q(city__icontains=city))

    if address is not None:
        if address.strip() != '':
            queryset = queryset.filter(Q(address__icontains=address))

    if is_valid_queryparam(telephone):
        queryset = queryset.filter(telephone=telephone)

    if is_valid_queryparam(postal_code):
        queryset = queryset.filter(postal_code=postal_code)

    return queryset

@login_required
def worker_details(request, worker_id):
    worker = get_object_or_404(Worker, id=worker_id)
    if worker.ong == request.user.ong:
        return render(request, 'workers/details.html', {'worker': worker})
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


@login_required
@asem_required
def user_list(request):
    objects = ASEMUser.objects.filter(ong=request.user.ong).values()

    paginator = Paginator(objects, 12)
    page_number = request.GET.get('page')
    user_page = paginator.get_page(page_number)

    title = "Gestión de Usuarios ASEM"
    form = FilterAsemUserForm()
    
    if request.method == 'GET':
        objects = asemuser_filter(objects, FilterAsemUserForm(request.GET))

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
        'form' : form,
    }

    return render(request, 'users/list.html', context)


def is_valid_queryparam(param):
    return param != "" and param is not None

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
            if q.strip() != "":
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
    if request.method == "POST":
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

    return render(request, 'person/godfather/form.html', {"form": form, "title": "Añadir Padrino"})


@login_required
@videssur_required
def godfather_update(request, godfather_id):
    godfather = get_object_or_404(GodFather, id=godfather_id)
    form = CreateNewGodFather(instance=godfather)
    if request.user.ong == godfather.ong:
        if request.method == "POST":
            form = CreateNewGodFather(
                request.POST or None, request.FILES or None, instance=godfather)
            if form.is_valid():
                try:
                    form.save()
                    return redirect("godfather_list")
                except ValidationErr as v:
                    messages.error(request, str(v.args[0]))
            else:
                messages.error(request, 'Formulario con errores')
    else:
        return custom_403(request)
    return render(request, 'person/godfather/form.html', {"form": form})


@login_required
@videssur_required
def godfather_details(request, godfather_id):
    godfather = get_object_or_404(GodFather, id=godfather_id)
    return render(request, 'prueba_padrino_detalles.html', {'godfather': godfather})


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
    if request.method == "POST":
        form = CreateNewChild(request.POST, request.FILES)
        if form.is_valid():
            ong = request.user.ong  # it is videssur basically
            child = form.save(commit=False)
            child.ong = ong
            child.save()
            return redirect('child_list')
        else:
            messages.error(request, 'Formulario con errores')
    return render(request, 'person/child/create_child.html', {"form": form, "title": "Añadir Niño"})


@login_required
@videssur_required
def child_update(request, child_id):
    child = get_object_or_404(Child, id=child_id)
    if request.user.ong == child.ong:
        form = CreateNewChild(instance=child)
        if request.method == "POST":
            form = CreateNewChild(request.POST or None,
                                  request.FILES or None, instance=child)
            if form.is_valid():
                try:
                    form.save()
                    return redirect("child_list")
                except ValidationErr as v:
                    messages.error(request, str(v.args[0]))
            else:
                messages.error(request, 'Formulario con errores')
    else:
        return custom_403(request)

    return render(request, 'person/child/create_child.html', {"form": form})


@login_required
@videssur_required
def child_details(request, child_id):
    child = get_object_or_404(Child, id=child_id)
    return render(request, 'user/details.html', {'child': child})


@login_required
@videssur_required
def child_delete(request, child_id):
    child = get_object_or_404(Child, id=child_id)
    child.delete()
    return redirect('child_list')


@login_required
def volunteer_list(request):
    objects = Volunteer.objects.filter(ong=request.user.ong).values()
    
    paginator = Paginator(objects, 12)
    page_number = request.GET.get('page')
    user_page = paginator.get_page(page_number)

    title = "Gestión de Voluntarios"
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
    }

    return render(request, 'users/list.html', context)


@login_required
def volunteer_details(request, volunteer_id):
    volunteer = get_object_or_404(Volunteer, id=volunteer_id)
    if volunteer.ong == request.user.ong:
        return render(request, 'volunteer_details.html', {'volunteer': volunteer})
    else:
        return custom_403(request)


@login_required
def volunteer_create(request):
    form = CreateNewVolunteer(initial={'ong': request.user.ong})
    if request.method == "POST":
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
    return render(request, 'volunteers/volunteers_form.html', {"form": form, "title": "Añadir Voluntario"})


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
        if request.method == "POST":
            form = CreateNewVolunteer(
                request.POST, request.FILES, instance=volunteer)

            if form.is_valid():
                form.save()
                return redirect('volunteer_list')
            else:
                messages.error(request, 'Formulario con errores')
    else:
        return custom_403(request)
    return render(request, 'volunteers/volunteers_form.html', {"form": form})

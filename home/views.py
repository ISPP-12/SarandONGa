from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import json
from django.core.paginator import Paginator
from .models import Home
from .models import PAYMENT_METHOD
from .models import FREQUENCY
from .forms import CreateHomeForm, FilterHomeForm
from decimal import Decimal
from datetime import date
from django.contrib.auth.decorators import login_required
from main.views import videssur_required
from xml.dom import ValidationErr
from django.db.models import Q


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.strftime('%d/%m/%Y')
        elif isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


@login_required
def home_create(request):
    form = CreateHomeForm()
    if request.method == 'POST':
        form = CreateHomeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home_list')
            except ValidationErr as v:
                messages.error(request, str(v.args[0]))
        else:
            messages.error(request, 'El formulario presenta errores')
    return render(request, 'home/home_form.html', {'form': form, 'page_title': 'SarandONGa 💃 - Añadir Casa'})

@login_required
def home_list(request):
    form = FilterHomeForm(request.GET or None)
    homes = Home.objects.all()

    if request.method == 'GET':
        homes = home_filter(homes, form)

    paginator = Paginator(homes, 12)
    page_number = request.GET.get('page')
    home_page = paginator.get_page(page_number)

    homes_dict = [obj.__dict__ for obj in home_page]
    for d in homes_dict:
        d.pop('_state', None)

    # choices to values
    for home in homes_dict:
        home['payment_method'] = dict(PAYMENT_METHOD)[home['payment_method']]
        home['frequency'] = dict(FREQUENCY)[home['frequency']]
        # remove null values
        for key, value in list(home.items()):
            if value is None or value == '':
                home[key] = '-'

    # json
    homes_json = json.dumps(homes_dict, cls=CustomJSONEncoder)

    query_str = "&qsearch="
    keys = request.GET.keys()
    if "qsearch" in keys:
        query_str += request.GET["qsearch"]

    context = {
        'objects': home_page,
        'objects_json': homes_json,
        'object_name': 'casa',
        'object_name_en': 'home',
        'title': 'Gestión de Casas',
        'page_title': 'SarandONGa 💃 - Gestión de Casas',
        'form': form,
        'query_str': query_str
    }

    return render(request, 'home/list.html', context)


@login_required
@videssur_required
def home_delete(request, home_id):
    home = get_object_or_404(Home, id=home_id)
    home.delete()
    return redirect('home_list')


@login_required
@videssur_required
def home_details(request, home_id):
    home = get_object_or_404(Home, id=home_id)
    return render(request, 'home/home_details.html', {'home': home})

@login_required
@videssur_required
def home_update(request,home_id):
    home_to_update = Home.objects.get(id=home_id)
    form = CreateHomeForm(instance=home_to_update)
    if request.method == "POST":
        form = CreateHomeForm(request.POST, instance=home_to_update)
        if form.is_valid():
            try:
                form.save()
                return redirect('home_list')
            except ValidationErr as v:
                    messages.error(request, str(v.args[0]))
        else:
            messages.error(request, 'Formulario con errores')
    return render(request, 'home/home_form.html', {"form": form, "page_title": "SarandONGa 💃 - Editar Casa"})

def is_valid_queryparam(param):
    return param != "" and param is not None

def home_filter(queryset, form):
    
    q = form['qsearch'].value()
    min_start_date = form['min_start_date'].value()
    max_start_date = form['max_start_date'].value()
    min_termination_date = form['min_termination_date'].value()
    max_termination_date = form['max_termination_date'].value()
    province = form['province'].value()
    bank_account_holder = form['bank_account_holder'].value()
    bank_account_reference = form['bank_account_reference'].value()
    payment_method = form['payment_method'].value()
    frequency = form['frequency'].value()
    amount_min = form['amount_min'].value()
    amount_max = form['amount_max'].value()
    

    if q is not None:
            if q.strip() != "":
                queryset = queryset.filter(
                    Q(name__icontains=q) |
                    Q(bank_account_number__icontains=q) |
                    Q(province__icontains=q) |
                    Q(bank_account_holder__icontains=q) |
                    Q(bank_account_reference__icontains=q)
                )

    if is_valid_queryparam(min_start_date):
        queryset = queryset.filter(start_date__gte=min_start_date)

    if is_valid_queryparam(max_start_date):
        queryset = queryset.filter(start_date__lte=max_start_date)

    if is_valid_queryparam(min_termination_date):
        queryset = queryset.filter(termination_date__gte=min_termination_date)

    if is_valid_queryparam(max_termination_date):
        queryset = queryset.filter(termination_date__lte=max_termination_date)

    if is_valid_queryparam(province):
        queryset = queryset.filter(province=province)

    if is_valid_queryparam(bank_account_holder):
        queryset = queryset.filter(bank_account_holder=bank_account_holder)

    if is_valid_queryparam(bank_account_reference):
        queryset = queryset.filter(bank_account_reference=bank_account_reference)

    if is_valid_queryparam(payment_method):
        queryset = queryset.filter(payment_method=payment_method)

    if is_valid_queryparam(frequency):
        queryset = queryset.filter(frequency=frequency)

    if is_valid_queryparam(amount_min):
        queryset = queryset.filter(amount__gte=amount_min)

    if is_valid_queryparam(amount_max):
        queryset = queryset.filter(amount__lte=amount_max)

    

    return queryset
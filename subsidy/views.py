from django.shortcuts import render, redirect, get_object_or_404
from .models import Subsidy
from .forms import CreateNewSubsidy, FilterSubsidyForm
from datetime import date
import json
from decimal import Decimal
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from main.views import custom_403
from django.db.models import Q


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.strftime('%d/%m/%Y')
        elif isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


@login_required
def subsidy_create(request):
    form = CreateNewSubsidy(initial={'ong': request.user.ong})
    if request.method == "POST":
        form = CreateNewSubsidy(request.POST, request.FILES)

        if form.is_valid():
            ong = request.user.ong
            subsidy = form.save(commit=False)
            subsidy.ong = ong
            subsidy.save()
            form.save()

            return redirect("/subsidy/list")
        else:
            messages.error(request, 'Formulario con errores')

    return render(request, 'subsidy/create.html', {"form": form, "object_name": "subvención",  "title": "Añadir Subvención", 'page_title': 'SarandONGa 💃 - Añadir Subvención'})


@login_required
def subsidy_list(request):
    subsidies = Subsidy.objects.filter(
        ong=request.user.ong).order_by('-presentation_date').values()

    form = FilterSubsidyForm(request.GET or None)

    if request.method == 'GET':
        subsidies = subsidy_filter(subsidies, form)

    paginator = Paginator(subsidies, 12)
    page_number = request.GET.get('page')
    subsidies_page = paginator.get_page(page_number)

    # depending of the user type write one title or another
    subsidies_dict = [user for user in subsidies_page]

    for s in subsidies_dict:
        s.pop('_state', None)
        # remove null values
        for key, value in list(s.items()):
            if value is None or value == '':
                s[key] = '-'

    subsidies_json = json.dumps(subsidies_dict, cls=CustomJSONEncoder)

    query_str = ""
    keys = request.GET.keys()
    if "qsearch" in keys:
        query_str = "&qsearch="
        query_str += request.GET["qsearch"]
    if "min_presentation_date" in keys:
        query_str += "&min_presentation_date="
        query_str += request.GET["min_presentation_date"]
    if "max_presentation_date" in keys:
        query_str += "&max_presentation_date="
        query_str += request.GET["max_presentation_date"]
    if "min_payment_date" in keys:
        query_str += "&min_payment_date="
        query_str += request.GET["min_payment_date"]
    if "max_payment_date" in keys:
        query_str += "&max_payment_date="
        query_str += request.GET["max_payment_date"]
    if "min_provisional_resolution_date" in keys:
        query_str += "&min_provisional_resolution_date="
        query_str += request.GET["min_provisional_resolution_date"]
    if "max_final_resolution_date" in keys:
        query_str += "&max_final_resolution_date="
        query_str += request.GET["max_final_resolution_date"]
    if "organism" in keys:
        query_str += "&organism="
        query_str += request.GET["organism"]
    if "name" in keys:
        query_str += "&name="
        query_str += request.GET["name"]
    if "status" in keys:
        query_str += "&status="
        query_str += request.GET["status"]
    if "amount_min" in keys:
        query_str += "&amount_min="
        query_str += request.GET["amount_min"]
    if "amount_max" in keys:
        query_str += "&amount_max="
        query_str += request.GET["amount_max"]

    context = {
        'objects': subsidies_page,
        'objects_json': subsidies_json,
        'object_name': 'subvención',
        'object_name_en': 'subsidy',
        'title': 'Gestión de Subvenciones',
        'page_title': 'SarandONGa 💃 - Gestión de Subvenciones',
        'form': form,
        'query_str': query_str
    }

    return render(request, 'subsidy/list.html', context)


@login_required
def subsidy_delete(request, subsidy_id):
    subsidy = get_object_or_404(Subsidy, id=subsidy_id)
    if subsidy.ong == request.user.ong:
        subsidy.delete()
    else:
        return custom_403(request)
    return redirect("/subsidy/list")


@login_required
def subsidy_update(request, subsidy_id):
    subsidy = get_object_or_404(Subsidy, id=subsidy_id)

    if request.user.ong == subsidy.ong:
        form = CreateNewSubsidy(instance=subsidy)
        if request.method == "POST":
            form = CreateNewSubsidy(
                request.POST,  request.FILES, instance=subsidy)
            if form.is_valid():
                form.save()
                return redirect("/subsidy/list")
            else:
                messages.error(request, 'Formulario con errores')
    else:
        return custom_403(request)
    return render(request, 'subsidy/create.html', {"form": form, 'page_title': 'SarandONGa 💃 - Editar Subvención'})


def is_valid_queryparam(param):
    return param != "" and param is not None


def subsidy_filter(queryset, form):

    q = form['qsearch'].value()
    min_presentation_date = form['min_presentation_date'].value()
    max_presentation_date = form['max_presentation_date'].value()
    min_payment_date = form['min_payment_date'].value()
    max_payment_date = form['max_payment_date'].value()
    min_provisional_resolution_date = form['min_provisional_resolution_date'].value(
    )
    max_provisional_resolution_date = form['max_provisional_resolution_date'].value(
    )
    min_final_resolution_date = form['min_final_resolution_date'].value()
    max_final_resolution_date = form['max_final_resolution_date'].value()
    organism = form['organism'].value()
    name = form['name'].value()
    status = form['status'].value()
    amount_min = form['amount_min'].value()
    amount_max = form['amount_max'].value()

    if q is not None:
        if q.strip() != "":
            queryset = queryset.filter(
                Q(organism__icontains=q) |
                Q(status__icontains=q) |
                Q(name__icontains=q)
            )

    if is_valid_queryparam(min_presentation_date):
        queryset = queryset.filter(
            presentation_date__gte=min_presentation_date)

    if is_valid_queryparam(max_presentation_date):
        queryset = queryset.filter(
            presentation_date__lte=max_presentation_date)

    if is_valid_queryparam(min_payment_date):
        queryset = queryset.filter(payment_date__gte=min_payment_date)

    if is_valid_queryparam(max_payment_date):
        queryset = queryset.filter(payment_date__lte=max_payment_date)

    if is_valid_queryparam(min_provisional_resolution_date):
        queryset = queryset.filter(
            provisional_resolution__gte=min_provisional_resolution_date)

    if is_valid_queryparam(max_provisional_resolution_date):
        queryset = queryset.filter(
            provisional_resolution__lte=max_provisional_resolution_date)

    if is_valid_queryparam(min_final_resolution_date):
        queryset = queryset.filter(
            final_resolution__gte=min_final_resolution_date)

    if is_valid_queryparam(max_final_resolution_date):
        queryset = queryset.filter(
            final_resolution__lte=max_final_resolution_date)

    if is_valid_queryparam(organism):
        queryset = queryset.filter(organism=organism)

    if is_valid_queryparam(name):
        queryset = queryset.filter(name=name)

    if is_valid_queryparam(status):
        queryset = queryset.filter(status=status)

    if is_valid_queryparam(amount_min):
        queryset = queryset.filter(amount__gte=amount_min)

    if is_valid_queryparam(amount_max):
        queryset = queryset.filter(amount__lte=amount_max)

    return queryset

from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime, date
import json
from donation.models import Donation
from decimal import Decimal
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateNewDonation, FilterDonationForm
from main.views import custom_403
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
def donation_create(request):
    form = CreateNewDonation(initial={'ong': request.user.ong})
    if request.method == "POST":
        form = CreateNewDonation(request.POST, request.FILES)
        if form.is_valid():
            ong = request.user.ong
            donation = form.save(commit=False)
            donation.ong = ong
            donation.save()
            form.save()
            return redirect('/donation/list')
        else:
            messages.error(request, 'Formulario con errores')

    return render(request, 'donation/create.html', {'object_name': 'donate', "form": form, "button_text": "Registrar donación", "page_title": "SarandONGa 💃 - Añadir donación"})


@login_required
def donation_list(request):
    # get donations from database
    objects = Donation.objects.filter(
        ong=request.user.ong).order_by('-created_date').values()

    form = FilterDonationForm(request.GET or None)
    if request.method == 'GET':
        objects = donation_filter(objects, form)

    paginator = Paginator(objects, 12)
    page_number = request.GET.get('page')
    donation_page = paginator.get_page(page_number)

    donations_dict = [donation for donation in donation_page]
    for donation in donations_dict:
        donation.pop('_state', None)
        # remove null values
        for key, value in list(donation.items()):
            if value is None or value == '':
                donation[key] = '-'

    donations_json = json.dumps(donations_dict, cls=CustomJSONEncoder)

    query_str = ""
    keys = request.GET.keys()
    if "qsearch" in keys:
        query_str = "&qsearch="
        query_str += request.GET["qsearch"]
    if "min_date" in keys:
        query_str += "&min_date="
        query_str += request.GET["min_date"]
    if "max_date" in keys:
        query_str += "&max_date="
        query_str += request.GET["max_date"]
    if "min_amount" in keys:
        query_str += "&min_amount="
        query_str += request.GET["min_amount"]
    if "max_amount" in keys:
        query_str += "&max_amount="
        query_str += request.GET["max_amount"]

    for donation in objects:
        created_date = donation["created_date"]
        modified_date = created_date.strftime('%d/%m/%Y %H:%M')
        donation["created_date"] = modified_date

    context = {
        'objects': donation_page,
        'objects_json': donations_json,
        'object_name': 'donación',
        'object_name_en': 'donation',
        'title': 'Gestión de Donaciones',
        'form': form,
        'query_str': query_str,
        'page_title': 'SarandONGa 💃 - Gestión de Donaciones'
    }

    return render(request, 'donation/list.html', context)


def is_valid_queryparam(param):
    return param != '' and param is not None


def donation_filter(queryset, form):

    q = form['qsearch'].value()
    min_date = form['min_date'].value()
    max_date = form['max_date'].value()
    min_amount = form['min_amount'].value()
    max_amount = form['max_amount'].value()

    if q is not None:
        if q.strip() != '':
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(description__icontains=q) |
                Q(donor_name__icontains=q) |
                Q(donor_surname__icontains=q) |
                Q(donor_dni__icontains=q) |
                Q(donor_address__icontains=q) |
                Q(donor_email__icontains=q)
            )

    if is_valid_queryparam(min_date):
        queryset = queryset.filter(created_date__gte=min_date)

    if is_valid_queryparam(max_date):
        queryset = queryset.filter(created_date__lte=max_date)

    if is_valid_queryparam(min_amount):
        queryset = queryset.filter(amount__gte=min_amount)

    if is_valid_queryparam(max_amount):
        queryset = queryset.filter(amount__lte=max_amount)

    return queryset


@login_required
def donation_update(request, donation_id):
    donation = get_object_or_404(Donation, id=donation_id)
    if request.user.ong == donation.ong:
        form = CreateNewDonation(instance=donation)
        if request.method == "POST":
            form = CreateNewDonation(
                request.POST,  request.FILES, instance=donation)
            if form.is_valid():
                form.save()
                return redirect("/donation/list")
            else:
                messages.error(request, 'Formulario con errores')
    else:
        return custom_403(request)
    return render(request, 'donation/create.html', {'object_name': 'donate', "form": form, "button_text": "Actualizar", 'page_title': 'SarandONGa 💃 - Actualizar Donación'})


@login_required
def donation_delete(request, donation_id):
    donation = get_object_or_404(Donation, id=donation_id)
    donation.delete()
    return redirect('donation_list')

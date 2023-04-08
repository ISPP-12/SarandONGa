from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
import json
from donation.models import Donation
from decimal import Decimal
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateNewDonation
from main.views import custom_403
from django.core.paginator import Paginator


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
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

    return render(request, 'donation/create.html', {'object_name': 'donate', "form": form, "button_text": "Registrar donación"})


@login_required
def donation_list(request):
    # get donations from database
    objects = Donation.objects.filter(
        ong=request.user.ong).order_by('-created_date').values()

    paginator = Paginator(objects, 12)
    page_number = request.GET.get('page')
    donation_page = paginator.get_page(page_number)

    donations_dict = [donation for donation in donation_page]
    for d in donations_dict:
        d.pop('_state', None)

    donations_json = json.dumps(donations_dict, cls=CustomJSONEncoder)

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
    }

    return render(request, 'donation/list.html', context)


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
    return render(request, 'donation/create.html', {'object_name': 'donate', "form": form, "button_text": "Actualizar"})


@login_required()
def donation_delete(request, donation_id):
    donation = get_object_or_404(Donation, id=donation_id)
    donation.delete()
    return redirect('donation_list')

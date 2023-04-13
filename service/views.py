from django.shortcuts import render, get_object_or_404, redirect
from .forms import CreateNewService
from .models import Service
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.views import asem_required
import json


@login_required
@asem_required
def service_create(request):
    form = CreateNewService(request.POST)
    if request.method == "POST":
        if form.is_valid():
            service = form.save(commit=False)
            service.save()
            return redirect('service_create')
        else:
            messages.error(request, 'El formulario presenta errores')
    
    else:
        services = Service.objects.all()
        events = []
        for event in services:
            event_sub_arr = {}
            event_sub_arr['title'] = f'{event.service_type} - {event.amount}'
            start_date = event.date
            end_date = event.date
            
            event_sub_arr['start'] = start_date
            event_sub_arr['end'] = end_date
            event_sub_arr['url'] = f'./{event.id}/update'
            event_sub_arr['id'] = str(event.id)
            events.append(event_sub_arr)
        events_json = json.dumps(events, default=str)

    context = {"form": form, "title": "Añadir Servicio", "events_json": events_json}
    
    return render(request, 'service/service_form.html', context)


@login_required
@asem_required
def service_list(request):

    context = {
        'objects': Service.objects.all(),
        'objects_json': '[]',
        'object_name': 'Servicio',
        'object_name_en': 'service',
        'title': 'Gestión de servicios',
    }

    return render(request, 'service_list.html', context)

@login_required
@asem_required
def service_update(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == "POST":
        form = CreateNewService(request.POST, request.FILES,instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
        else:
            messages.error(request, 'Formulario con errores')
    else: 
        form = CreateNewService(instance=service)
    return render(request, 'service/service_form_backend.html', {"form": form, "title": "Editar Servicio"})

@login_required
@asem_required
def service_delete(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service.delete()
    return redirect('service_list')

@login_required
@asem_required
def service_details(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'service/service_details.html', {'service': service})


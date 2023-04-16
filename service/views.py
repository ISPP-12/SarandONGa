from django.shortcuts import render, get_object_or_404, redirect
from .forms import CreateNewService
from .models import Service
from person.models import ASEMUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.views import asem_required
import json


@login_required
@asem_required
def service_create(request):
    if 'asem_user' in request.GET:
        user = ASEMUser.objects.get(id=request.GET.get('asem_user'))
    else:
        user = None
    if request.method == "POST":
        form = CreateNewService(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.save()
            return redirect('service_create')
        else:
            messages.error(request, 'El formulario presenta errores')
    
    else:
        initial_data = {'asem_user': user}
        form = CreateNewService(initial=initial_data)
        
        services = Service.objects.all()
        events = []
        for event in services:
            event_sub_arr = {}
            event_sub_arr['title'] = f'{event.service_type} - {event.amount}'
            start_date = event.date
            end_date = event.date
            
            event_sub_arr['start'] = start_date
            event_sub_arr['end'] = end_date
            event_sub_arr['url'] = f'/service/{event.id}/update'
            event_sub_arr['id'] = str(event.id)
            events.append(event_sub_arr)
        events_json = json.dumps(events, default=str)

    context = {
        "form": form, 
        "title": "Crear Servicio", 
        "events_json": events_json, 
        'page_title': 'SarandONGa 💃 - Crear Servicio'
        }
    
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
        'page_title': 'SarandONGa 💃 - Gestión de Servicios'
    }

    return render(request, 'service_list.html', context)

@login_required
@asem_required
def service_update(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    form = CreateNewService(instance=service)
    if request.method == "POST":
        form = CreateNewService(request.POST, request.FILES,instance=service)
        if form.is_valid():
            form.save()
            return redirect('/service/create')
        else:
            messages.error(request, 'Formulario con errores')
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
            event_sub_arr['url'] = f'/service/{event.id}/update'
            event_sub_arr['id'] = str(event.id)
            events.append(event_sub_arr)
        events_json = json.dumps(events, default=str)
        
    context = {
        'form': form, 
        'events_json': events_json,
        'title': "Editar Servicio", 
        'page_title': 'SarandONGa 💃 - Editar Servicio'
        }
        
    return render(request, 'service/service_form.html', context)

@login_required
@asem_required
def service_delete(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service.delete()
    return redirect('service_create')

@login_required
@asem_required  #TODO
def service_details(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'service/service_details.html', {'service': service})


from django.shortcuts import render, get_object_or_404, redirect
from .forms import CreateNewService
from .models import Service
from django.contrib import messages

def service_create(request):
    if request.method == "POST":
        form = CreateNewService(request.POST)
        if form.is_valid():
            form.save()
            return service_list(request)

    form = CreateNewService()
    return render(request, 'service/service_form_test.html', {"form": form, "title": "Crear Servicio"})


def service_list(request):

    context = {
        'objects': Service.objects.all(),
        'objects_json': '[]',
        'object_name': 'Servicio',
        'object_name_en': 'service',
        'title': 'Gestión de servicios',
    }

    return render(request, 'service_list.html', context)

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
    return render(request, 'service/service_form_test.html', {"form": form})
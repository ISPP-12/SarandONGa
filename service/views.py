from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewService
from .models import Service
from django.contrib.auth.decorators import login_required
from main.views import asem_required

@login_required
@asem_required
def service_create(request):
    if request.method == "POST":
        form = CreateNewService(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')

    form = CreateNewService()
    return render(request, 'service/service_form_backend.html', {"form": form, "title": "Crear Servicio"})

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
def service_delete(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service.delete()
    return redirect('service_list')

@login_required
@asem_required
def service_details(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'service/service_details.html', {'service': service})
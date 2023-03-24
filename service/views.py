from django.shortcuts import render, get_object_or_404
from .forms import CreateNewService
from .models import Service

def service_create(request):
    if request.method == "POST":
        form = CreateNewService(request.POST)
        if form.is_valid():
            form.save()
            return service_list(request)

    form = CreateNewService()
    return render(request, 'service/service_form.html', {"form": form, "title": "Crear Servicio"})


def service_list(request):

    context = {
        'objects': Service.objects.all(),
        'objects_json': '[]',
        'object_name': 'Servicio',
        'object_name_en': 'service',
        'title': 'Gestión de servicios',
    }

    return render(request, 'service_list.html', context)

def service_details(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'service/service_details.html', {'service': service})

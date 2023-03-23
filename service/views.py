from django.shortcuts import render
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

    return render(request, 'service/list.html', context)

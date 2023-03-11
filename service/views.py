from django.shortcuts import render
from .models import Service

def service_list(request):

    context = {
        'objects': Service.objects.all(),
        'objects_name': 'Servicio',
        'title': 'Gestión de servicios'
    }
    return render(request, 'service_list.html', {"context":context})


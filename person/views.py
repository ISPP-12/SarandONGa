from django.shortcuts import render
from .models import GodFather, ASEMUser
#import json

def godfather_list(request):

    context = {
        'objects': GodFather.objects.all(),
        #'objects_json' : json.dumps(list(GodFather.objects.all().values())),
        'objects_name': 'Padrino',
        'title': 'Gestión de padrinos'
    }
    return render(request, 'person/godfather_list.html', {"context":context})

def asem_user_list(request):
    objects = ASEMUser.objects.all().values()
    #objects_json = json.dumps(objects)
    object_name = 'usuario'
    title = "Gestion de Usuarios ASEM"
    return render(request, 'asem_user_list.html', {"objects":objects,"objects_name": object_name,"title":title })
from django.shortcuts import render
from .models import ASEMUser

def asem_user_list(request):
    objects = ASEMUser.objects.all().values()
    #objects_json = json.dumps(objects)
    object_name = 'usuario'
    title = "Gestion de Usuarios ASEM"
    return render(request, 'asem_user_list.html', {"objects":objects,"objects_name": object_name,"title":title })
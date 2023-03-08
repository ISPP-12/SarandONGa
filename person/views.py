from django.shortcuts import render
from .models import ASEMUser

def asem_user_list(request):
    asem_user_list=ASEMUser.objects.all().values()
    
    return render(request, 'asem_user_list.html', {"asem_user_list":asem_user_list })
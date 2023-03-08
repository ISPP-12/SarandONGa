from django.shortcuts import render

from person.models import GodFather

# Create your views here.

def show_workers(request):
    #Get all persons
    workers = GodFather.objects.all()
    return render(request, 'workers.html', {"workers": workers})

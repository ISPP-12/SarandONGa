
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewProyect
from django.contrib import messages
from proyect.models import Proyect
from django.shortcuts import render



def proyect_delete(request, proyect_id):
    proyect = get_object_or_404(Proyect, id=proyect_id)
    proyect.delete()
    return redirect('/')

def proyect_create(request):
    if request.method == "POST":
        form = CreateNewProyect(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    form = CreateNewProyect()
    return render(request, 'proyect/proyect_form.html', {"form": form, "title": "Crear Proyecto"})

def proyect_list(request):
    context = {
        'objects': Proyect.objects.all(),
        'object_name': 'proyect',
        'title': 'Lista de proyectos'
    }
    return render(request, 'proyect/list.html', {"context":context})


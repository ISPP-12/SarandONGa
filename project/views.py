from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewProject
from django.contrib import messages
from .models import Project
from django.contrib.auth.decorators import login_required
from main.views import videssur_required
import json
from datetime import date
from decimal import Decimal

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.strftime('%d/%m/%Y')
        elif isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)

@login_required
@videssur_required
def project_delete(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('/')

@login_required
@videssur_required
def project_create(request):
    if request.method == "POST":
        form = CreateNewProject(request.POST, initial={'ong':request.user.ong})
        if form.is_valid():
            project = form.save(commit=False)
            project.ong = request.user.ong
            project.save()
            return redirect('/')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    form = CreateNewProject()
    return render(request, 'project/project_form.html', {"form": form, "title": "Crear Proyecto"})

@login_required
@videssur_required
def project_update(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == "POST":
        form = CreateNewProject(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
           for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    form = CreateNewProject(instance=project)
    return render(request, 'project/project_form.html', {'form': form, 'title': 'Actualizar proyecto'})

@login_required
@videssur_required
def project_details(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'project/project_details.html', {'project': project})

@login_required
@videssur_required
def project_list(request):
    context = {
        'objects': Project.objects.filter(ong=request.user.ong).values(),
        'objects_json' : json.dumps(list(Project.objects.filter(ong=request.user.ong).values()), cls=CustomJSONEncoder),
        'object_name': 'proyecto',
        'object_name_en': 'project',
        'title': 'Gestión de proyectos',
    }
    return render(request, 'project/list.html', context)
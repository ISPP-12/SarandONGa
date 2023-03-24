
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewProject
from django.contrib import messages
from .models import Project


def project_delete(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('/')


def project_create(request):
    if request.method == "POST":
        form = CreateNewProject(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    form = CreateNewProject()
    return render(request, 'project/project_form.html', {"form": form, "title": "Crear Proyecto"})


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

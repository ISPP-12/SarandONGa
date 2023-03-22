from django.shortcuts import render, redirect
from .forms import CreateNewProyect
from django.contrib import messages

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
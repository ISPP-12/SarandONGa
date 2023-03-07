from django.shortcuts import render
from .forms import CreateNewGodFather
from django.contrib import messages

def godfather_create(request):
    if request.method == "POST":
        form = CreateNewGodFather(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, 'Formulario con errores')

    form = CreateNewGodFather()
    return render(request, 'godfather_form.html', {"form": form})
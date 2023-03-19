from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Home
from .forms import create_home_form

def home_create(request):
    if request.method == 'POST':
        form = create_home_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, 'El formulario presenta errores')
    else:
        form = create_home_form()
    return render(request, 'home/home_form.html', {'form': form})



def home_list(request):
    context = {
        'objects': Home.objects.all(),
        #'objects_json': json.dumps(list(Payment.objects.all().values())),
        'objects_name': 'Home',
        'title': 'Lista de Casas'
    }
    return render(request, 'home/home_list.html', {"context":context })

def home_delete(request, slug):
    home = Home.objects.get(slug=slug)
    home.delete()
    return redirect('home_list')

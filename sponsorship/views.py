from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Sponsorship
from .forms import create_sponsorship_form

def sponsorship_create(request):
    if request.method == 'POST':
        form = create_sponsorship_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, 'El formulario presenta errores')
    else:
        form = create_sponsorship_form()
    return render(request, 'sponsorship/sponsorship_form.html', {'form': form})



def sponsorship_list(request):
    context = {
        'objects': Sponsorship.objects.all(),
        #'objects_json': json.dumps(list(Payment.objects.all().values())),
        'objects_name': 'Sponsorship',
        'title': 'Lista de Apadrinamientos'
    }
    return render(request, 'sponsorship/sponsorship_list.html', {"context":context })

def sponsorship_delete(request, sponsorship_slug):
    sponsorship = Sponsorship.objects.get(slug=sponsorship_slug)
    
    sponsorship.delete()
    return redirect('sponsorship_list')
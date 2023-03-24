from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from functools import wraps
from .models import Sponsorship
from .forms import create_sponsorship_form

def videssur_required(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if request.user.ong.name.lower() == "videssur":
            return function(request, *args, **kwargs)
        else:
            return redirect("/")
    return wrapper


@login_required(login_url='/admin/login/?next=/sponsorship/create/')
@videssur_required
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

@login_required(login_url='/admin/login/?next=/sponsorship/')
@videssur_required
def sponsorship_list(request):
    context = {
        'objects': Sponsorship.objects.all(),
        #'objects_json': json.dumps(list(Payment.objects.all().values())),
        'objects_name': 'Sponsorship',
        'title': 'Lista de Apadrinamientos'
    }
    return render(request, 'sponsorship/sponsorship_list.html', {"context":context })

@login_required(login_url='/admin/login/?next=/sponsorship/')
@videssur_required
def sponsorship_delete(request, sponsorship_slug):
    sponsorship = Sponsorship.objects.get(slug=sponsorship_slug)
    sponsorship.delete()
    return redirect('sponsorship_list')

@login_required(login_url='/admin/login/?next=/sponsorship/')
@videssur_required
def sponsorship_details(request, sponsorship_slug):
    sponsorship = get_object_or_404(Sponsorship, slug=sponsorship_slug)
    return render(request, 'sponsorship/sponsorship_details.html', {'sponsorship': sponsorship})
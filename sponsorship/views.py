from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Sponsorship
from .forms import create_sponsorship_form
from xml.dom import ValidationErr
from main.views import videssur_required




@login_required
@videssur_required
def sponsorship_create(request):
    if request.method == 'POST':
        form = create_sponsorship_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sponsorship_list')
        else:
            messages.error(request, 'El formulario presenta errores')
    else:
        form = create_sponsorship_form()
    return render(request, 'sponsorship/sponsorship_form.html', {'form': form})

@login_required
@videssur_required
def sponsorship_list(request):
    context = {
        'objects': Sponsorship.objects.all(),
        #'objects_json': json.dumps(list(Payment.objects.all().values())),
        'objects_name': 'Sponsorship',
        'title': 'Lista de Apadrinamientos'
    }
    return render(request, 'sponsorship/sponsorship_list.html', {"context":context })

@login_required
@videssur_required
def sponsorship_delete(request, sponsorship_id):
    sponsorship = Sponsorship.objects.get(id=sponsorship_id)
    sponsorship.delete()
    return redirect('sponsorship_list')

@login_required
@videssur_required
def sponsorship_details(request, sponsorship_slug):
    sponsorship = get_object_or_404(Sponsorship, slug=sponsorship_slug)
    return render(request, 'sponsorship/sponsorship_details.html', {'sponsorship': sponsorship})

@login_required
@videssur_required
def sponsorship_edit(request, sponsorship_slug):
    sponsorship_toupdate = get_object_or_404(Sponsorship, slug=sponsorship_slug)
    if request.method == "POST":
        form = create_sponsorship_form(request.POST or None,request.FILES or None ,instance=sponsorship_toupdate)
        if form.is_valid():
                try:
                    form.save()
                    return redirect('sponsorship_list')
                except ValidationErr as v:
                    messages.error(request, str(v.args[0]))
        else:
            messages.error(request, 'Formulario con errores')
    else:
        form = create_sponsorship_form(instance=sponsorship_toupdate)
    return render(request, 'sponsorship/sponsorship_form.html', {"form": form})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Sponsorship
from .forms import CreateSponsorshipForm
from main.views import videssur_required
from django.contrib.auth.decorators import login_required


@login_required
@videssur_required
def sponsorship_create(request):
    if request.method == 'POST':
        form = CreateSponsorshipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sponsorship_list')

        else:
            messages.error(request, 'El formulario presenta errores')
    else:
        form = CreateSponsorshipForm()
    return render(request, 'sponsorship/sponsorship_form.html', {'form': form})


@login_required
@videssur_required
def sponsorship_list(request):
    context = {
        'objects': Sponsorship.objects.all(),
        # 'objects_json': json.dumps(list(Payment.objects.all().values())),
        'objects_name': 'Sponsorship',
        'title': 'Lista de Apadrinamientos'
    }
    return render(request, 'sponsorship/sponsorship_list.html', {"context": context})


@login_required
@videssur_required
def sponsorship_delete(request, sponsorship_id):
    sponsorship = Sponsorship.objects.get(id=sponsorship_id)
    sponsorship.delete()
    return redirect('sponsorship_list')


@login_required
@videssur_required
def sponsorship_details(request, sponsorship_id):
    sponsorship = get_object_or_404(Sponsorship, id=sponsorship_id)
    return render(request, 'sponsorship/sponsorship_details.html', {'sponsorship': sponsorship})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from person.models import Child, GodFather
from .models import Sponsorship
from .forms import CreateSponsorshipForm
from xml.dom import ValidationErr
from main.views import  videssur_required


@login_required
@videssur_required
 
def sponsorship_create(request):
    #check if "child" is in the request:
    if 'child' in request.GET:
        child = Child.objects.get(id=request.GET.get('child'))
        active_sponsorship_exist = Sponsorship.objects.filter(child=child, termination_date=None).exists()
        if active_sponsorship_exist:
            sponsorship_id = Sponsorship.objects.filter(child=child, termination_date=None).get().id
            return sponsorship_edit(request, sponsorship_id)
    else:
        child = None
    if 'godfather' in request.GET:
        godfather = GodFather.objects.get(id=request.GET.get("godfather"))
    else:
        godfather = None

    if request.method == 'POST':
        form = CreateSponsorshipForm(request.POST)
        if form.is_valid():
            sponsorship = form.save(commit=False)
            sponsorship.save()
            form.save_m2m()
            return redirect('sponsorship_list')
        else:
            messages.error(request, 'El formulario presenta errores')
    else:
        initial_data = {'child': child, 'godfather': godfather}
        form = CreateSponsorshipForm(initial=initial_data)

    return render(request, 'sponsorship/sponsorship_form.html', {'form': form})



@login_required
@videssur_required
 
def sponsorship_list(request):
    context = {
        'objects': Sponsorship.objects.all(),
        # 'objects_json': json.dumps(list(Payment.objects.all().values())),
        'objects_name': 'Sponsorship',
        'title': 'Gestión de Apadrinamientos'
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

# def sponsorship_details(request, sponsorship_slug):
#    sponsorship = get_object_or_404(Sponsorship, slug=sponsorship_slug)
#    return render(request, 'sponsorship/sponsorship_details.html', {'sponsorship': sponsorship})


@login_required
@videssur_required
 
def sponsorship_edit(request, sponsorship_id):
    sponsorship_toupdate = get_object_or_404(Sponsorship, id=sponsorship_id)
    if request.method == "POST":
        form = CreateSponsorshipForm(
            request.POST or None, request.FILES or None, instance=sponsorship_toupdate)
        if form.is_valid():
            try:
                form.save()
                return redirect('sponsorship_list')
            except ValidationErr as v:
                messages.error(request, str(v.args[0]))
        else:
            messages.error(request, 'Formulario con errores')
    else:
        form = CreateSponsorshipForm(instance=sponsorship_toupdate)
    return render(request, 'sponsorship/sponsorship_form.html', {"form": form})

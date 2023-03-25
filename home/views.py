from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Home
from .forms import CreateHomeForm
from django.contrib.auth.decorators import login_required
from main.views import videssur_required
from xml.dom import ValidationErr

@login_required
@videssur_required
def home_create(request):
    form = CreateHomeForm()
    if request.method == 'POST':
        form = CreateHomeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home_list')
            except ValidationErr as v:
                messages.error(request, str(v.args[0]))
        else:
            messages.error(request, 'El formulario presenta errores')
    return render(request, 'home/home_form.html', {'form': form})

@login_required
@videssur_required
def home_list(request):
    context = {
        'objects': Home.objects.all(),
        # 'objects_json': json.dumps(list(Payment.objects.all().values())),
        'objects_name': 'Home',
        'title': 'Lista de Casas'
    }
    return render(request, 'home/home_list.html', {"context": context})

@login_required
@videssur_required
def home_delete(request, home_id):
    home = get_object_or_404(Home, id=home_id)
    home.delete()
    return redirect('home_list')

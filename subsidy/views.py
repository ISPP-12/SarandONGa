from django.shortcuts import render
from .models import Subsidy

from .forms import CreateNewSubsidy

# Create your views here.


def subsidy_create(request):
    if request.method == "POST":
        form = CreateNewSubsidy(request.POST)
        if form.is_valid():
            form.save()

    form = CreateNewSubsidy()
    return render(request, 'subsidy_form.html', {"form": form})


def subsidy_list(request):

    context = {
        'objects': Subsidy.objects.all().values(),
        'objects_name': 'Subvención',
        'title': 'Listado de Subvenciones',
    }

    return render(request, 'subsidy_list.html', context)

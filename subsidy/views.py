from django.shortcuts import render
from .models import Subsidy

from .forms import CreateNewSubsidy

# Create your views here.


def subsidy(request):
    if request.method == "POST":
        form = CreateNewSubsidy(request.POST)
        if form.is_valid():
            form.save()

    form = CreateNewSubsidy()
    return render(request, 'subsidy_form.html', {"form": form})


def subsidy_list(request):
    subsidy_list=Subsidy.objects.all().values()


    return render(request, 'subsidy_list.html', {"subsidy_list":subsidy_list })
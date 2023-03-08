from django.shortcuts import render

from .forms import CreateNewSubsidy

# Create your views here.


def subsidy(request):
    if request.method == "POST":
        form = CreateNewSubsidy(request.POST)
        if form.is_valid():
            form.save()

    form = CreateNewSubsidy()
    return render(request, 'subsidy_form.html', {"form": form})

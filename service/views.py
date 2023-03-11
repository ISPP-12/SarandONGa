from django.shortcuts import render
from .forms import CreateNewService


def service(request):
    if request.method == "POST":
        form = CreateNewService(request.POST)
        if form.is_valid():
            form.save()

    form = CreateNewService()
    return render(request, 'service/service_form.html', {"form": form})



from django.shortcuts import render
from donation.models import Donation

from donation.models import Donation
from .forms import CreateNewDonation

# Create your views here.
def donation(request):
    if request.method == "POST":
        form = CreateNewDonation(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            created_date = form.cleaned_data["created_date"]
            amount = form.cleaned_data["amount"]
            donor_name = form.cleaned_data["donor_name"]
            donor_surname = form.cleaned_data["donor_surname"]
            donor_email = form.cleaned_data["donor_email"]
            d = Donation(title= title, description=description, created_date=created_date,
                        amount=amount, donor_name=donor_name, donor_surname=donor_surname, donor_email=donor_email)
            d.save()

    form = CreateNewDonation()
    return render(request, 'donation_form.html', {"form": form})


def donationList(request):
    return render(request, "donation/donation_list.html" , {"donations": Donation.objects.all().values()})

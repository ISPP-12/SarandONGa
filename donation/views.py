from django.shortcuts import render
from donation.models import Donation

# Create your views here.

def donationList(request):
    return render(request, "donation/donation_list.html" , {"donations": Donation.objects.all().values()})

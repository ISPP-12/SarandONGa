from django.shortcuts import render
from .models import Volunteer

# Create your views here.
def VolunteersList(request):
    return render(request, "volunteer/volunteer_list.html" , {"volunteers": Volunteer.objects.all().values()})

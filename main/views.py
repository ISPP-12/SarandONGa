from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def donation(request):
    return render(request, 'donation_form.html')
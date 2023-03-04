from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def stock_register(request):
    return render(request,'stock/register.html')

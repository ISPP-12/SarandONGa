from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def stock_list(request):
    return render(request,'stock/list.html')
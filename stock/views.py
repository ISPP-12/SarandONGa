from django.shortcuts import render
from .models import Stock
from .forms import CreateNewStock
from django.views.decorators.csrf import csrf_exempt
#import json
# Create your views here.

def stock_list(request):

    context = {
        'objects': Stock.objects.all(),
        #'objects_json' : json.dumps(list(Stock.objects.all().values())),
        'objects_name' : 'Stock',
        'title': 'Lista de Stocks'
    }
    return render(request, 'stock/list.html', {"context":context })
 

def stock_create(request):
    if request.method == "POST":
        form = CreateNewStock(request.POST,request.FILES)
        if form.is_valid():
            name = form.cleaned_data["name"]
            quantity = form.cleaned_data["quantity"]
            d = Stock(name = name, quantity = quantity)
            d.save()
    form = CreateNewStock()
    return render(request, 'stock/register.html', {'form': form})
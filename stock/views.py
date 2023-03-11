from django.shortcuts import render
from .models import Stock
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
    
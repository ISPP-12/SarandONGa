from django.shortcuts import render, redirect, get_object_or_404
from .models import Stock
from .forms import CreateNewStock

def stock_list(request):

    context = {
        'objects': Stock.objects.all(),
        #'objects_json' : json.dumps(list(Stock.objects.all().values())),
        'object_name': 'stock',
        'title': 'Lista de stock',
    }
    return render(request, 'stock/list.html', context)


def stock_create(request):
    if request.method == "POST":
        form = CreateNewStock(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            quantity = form.cleaned_data["quantity"]
            d = Stock(name = name, quantity = quantity)
            d.save()
            return redirect('stock_list')
    form = CreateNewStock()
    return render(request, 'stock/register.html', {'form': form, 'title': 'Registrar artículo'})

def stock_delete(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id)
    stock.delete()
    return redirect('stock_list')
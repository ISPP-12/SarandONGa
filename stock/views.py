from django.shortcuts import render, redirect, get_object_or_404
from .models import Stock
from django.contrib import messages
from .forms import CreateNewStock
from django.contrib.auth.decorators import login_required
from main.views import custom_403
import json
from decimal import Decimal

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)

@login_required
 
def stock_list(request):

    stock = Stock.objects.filter(ong=request.user.ong).values()
    stock_dict = [obj for obj in stock]
    for d in stock_dict:
        d.pop('_state', None)

    stock_json = json.dumps(stock_dict, cls=CustomJSONEncoder)

    context = {
        'objects': stock,
        'objects_json' : stock_json,
        'object_name': 'stock',
        'page_title': 'SarandONGa 💃 - Gestión de inventario',
        'title': 'Gestión de inventario'
    }
    return render(request, 'stock/list.html', context)

@login_required
 
def stock_create(request):
    form = CreateNewStock(initial={'ong': request.user.ong})
    if request.method == "POST":
        form = CreateNewStock(request.POST, request.FILES)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.ong = request.user.ong
            stock.save()
            return redirect('stock_list')
        else:
            return custom_403(request)
    return render(request, 'stock/register.html', {'form': form, 'title': 'Registrar artículo', 'page_title': 'SarandONGa 💃 - Registrar artículo'})

@login_required
 
def stock_delete(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id)
    stock.delete()
    return redirect('stock_list')

@login_required
 
def stock_update(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id)
    if stock.ong == request.user.ong:
        if request.method == "POST":
            form = CreateNewStock(request.POST, request.FILES, instance=stock)
            if form.is_valid():
                form.save()
                return redirect('stock_list')
            else:
                messages.error(request, 'Formulario con errores')

        form = CreateNewStock(instance=stock)
        context = {'form': form, 'title': 'Actualizar artículo', 'page_title': 'SarandONGa 💃 - Actualizar artículo'}
    else:
        return custom_403(request)
    return render(request, 'stock/register.html', context)

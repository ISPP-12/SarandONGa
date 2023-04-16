from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Stock
from django.contrib import messages
from .forms import CreateNewStock, FilterStockForm
from django.contrib.auth.decorators import login_required
from main.views import custom_403
import json
from decimal import Decimal
from django.core.paginator import Paginator
from django.db.models import Q


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


@login_required
def stock_list(request):
    objects = Stock.objects.filter(ong=request.user.ong).values()

    form = FilterStockForm(request.GET or None)
    if request.method == 'GET':
        objects = stock_filter(objects, form)

    paginator = Paginator(objects, 9)
    page_number = request.GET.get('page')
    stock_page = paginator.get_page(page_number)

    stock_dict = [stock for stock in stock_page]
    for d in stock_dict:
        d.pop('_state', None)

    stock_json = json.dumps(stock_dict, cls=CustomJSONEncoder)

    query_str = "&qsearch="
    keys = request.GET.keys()
    if "qsearch" in keys:
        query_str += request.GET["qsearch"]
    query_str += "&min_quantity="
    if "min_quantity" in keys:
        query_str += request.GET["min_quantity"]
    query_str += "&max_quantity="
    if "max_quantity" in keys:
        query_str += request.GET["max_quantity"]
    query_str += "&min_amount="
    if "min_amount" in keys:
        query_str += request.GET["min_amount"]
    query_str += "&max_amount="
    if "max_amount" in keys:
        query_str += request.GET["max_amount"]

    context = {
        'objects': stock_page,
        'objects_json': stock_json,
        'object_name': 'stock',
        'page_title': 'SarandONGa 💃 - Gestión de inventario',
        'title': 'Gestión de inventario',
        'form': form,
        'query_str': query_str,
    }
    return render(request, 'stock/list.html', context)


def is_valid_queryparam(param):
    return param != '' and param is not None


def stock_filter(queryset, form):

    q = form['qsearch'].value()
    min_quantity = form['min_quantity'].value()
    max_quantity = form['max_quantity'].value()
    min_amount = form['min_amount'].value()
    max_amount = form['max_amount'].value()

    if q is not None:
        if q.strip() != '':
            queryset = queryset.filter(
                Q(name__icontains=q) |
                Q(model__icontains=q)
            )

    if is_valid_queryparam(min_quantity):
        queryset = queryset.filter(quantity__gte=min_quantity)

    if is_valid_queryparam(max_quantity):
        queryset = queryset.filter(quantity__lte=max_quantity)

    if is_valid_queryparam(min_amount):
        queryset = queryset.filter(amount__gte=min_amount)

    if is_valid_queryparam(max_amount):
        queryset = queryset.filter(amount__lte=max_amount)

    return queryset


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

def getStock(request):
    stock = Stock.objects.filter(ong=request.user.ong).values('name','quantity')
    return JsonResponse(list(stock), safe=False)

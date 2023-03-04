from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def stock_list(request):
    return render(request,'stock/list.html',{"stock":[{"name":"Nuevo","slug":"nuevo","amount":12},{"name":"Nuevo","slug":"nuevo-2","amount":12},{"name":"NuevoDEMASIAADASAOADOADOAODAODO","slug":"nuevo-3","amount":1}]})
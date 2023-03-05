from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def workers_list(request):
    return render(request,'workers/list.html',{"workers":[{"name":"Ramiro","surnames":"Pérez Reverte","image":"img\someone.png"},{"name":"Ramiro","surnames":"Pérez Reverte","image":"img\someone.png"},{"name":"Ramiro","surnames":"Pérez Reverte","image":"img\someone.png"}]})

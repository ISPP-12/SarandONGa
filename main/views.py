from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def grants_list(request):
    return render(
        request,
        'grants/list.html',
        {
            "grants":
            [
                {"name": "Ramiro", "surnames": "Pérez Reverte", "image": "img\someone.png"},
                {"name": "Ramiro", "surnames": "Pérez Reverte", "image": "img\someone.png"},
                {"name": "Ramiro", "surnames": "Pérez Reverte", "image": "img\someone.png"},
            ]
        }
    )
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')

    context = {
            'options1': {'1':'1','2':'2','3':'3','4':'4'},
            'options2': {'4':'5','9':'8'},
        }
    return render(request, 'index.html', context)


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

from django.shortcuts import render


def index(request):

    return render(request, 'index.html')


def components(request):
    
    context = {
        'options1': {'1':'1','2':'2','3':'3','4':'4'},
        'options2': {'4':'5','9':'8'},
        'stockTest': {'name':'STOCKINGS','quantity':9999},
        'object_name': 'ejemplo',
    }
    
    return render(request, 'components.html', context)

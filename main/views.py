from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
    'options1': {'1':'1','2':'2','3':'3','4':'4'},
    'options2': {'4':'5','9':'8'},}
    return render(request, 'index.html' ,context)
from django.urls import path
from . import views

urlpatterns = [
    path('create',views.proyect_create, name='proyect_create'),
]
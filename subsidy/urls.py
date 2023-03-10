from django.urls import path
from . import views

urlpatterns = [
    path('', views.subsidies_list, name='subsidies_list')
]

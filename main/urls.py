from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('stock/',views.stock_list, name='stock_list')
]
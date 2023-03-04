from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('stock-register/',views.stock_register, name='stock_register')
]

from django.urls import path
from . import views

urlpatterns = [
    path('list', views.stock_list, name="stock_list"),
    path('create', views.stock_create, name="stock_create"),


]

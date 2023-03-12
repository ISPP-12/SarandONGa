from django.urls import path
from . import views

urlpatterns = [
    path('list',views.donation_list, name='donation_list'),
    path('create', views.donation_create, name='donation_create')
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('workers/',views.workers_list, name='workers_list')
]
from django.urls import path
from . import views

urlpatterns = [
    path('workers/',views.workers_list, name='workers_list'),
    path('volunteers/',views.volunteers_list, name='volunteers_list'),
]
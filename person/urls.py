from django.urls import path
from . import views

urlpatterns = [
    path('workers/', views.workers_list, name='workers_list'),
    path('children/', views.children_list, name='children_list'),
]

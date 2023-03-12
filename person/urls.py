from django.urls import path
from . import views

urlpatterns = [
    path('workers/', views.workers_list, name='workers_list'),
    path('workers/create', views.create_worker, name="workers_create")
]

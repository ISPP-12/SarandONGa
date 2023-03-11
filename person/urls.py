from django.urls import path
from . import views

urlpatterns = [
    path('workers/',views.workers_list, name='workers_list'),
    path('worker/create', views.create_worker, name="worker"),
    path('asem_user/', views.asem_user, name="asem_user"),
    path('asem/asem_user_list', views.asem_user_list, name="asem_user_list"),
]
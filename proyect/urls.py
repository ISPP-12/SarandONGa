from django.urls import path
from . import views

urlpatterns = [
    path('create',views.proyect_create, name='proyect_create'),
    path('list',views.proyect_list, name='proyect_list'),
    path('<int:proyect_id>/delete',
        views.proyect_delete, name="proyect_delete"),
]
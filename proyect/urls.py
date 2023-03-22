from django.urls import path
from . import views

urlpatterns = [
    path('<int:proyect_id>/delete',
        views.proyect_delete, name="proyect_delete"),
]
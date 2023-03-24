from django.urls import path
from . import views

urlpatterns = [
    path('create', views.project_create, name='project_create'),
    path('<int:project_id>/delete',
         views.project_delete, name="project_delete"),
]

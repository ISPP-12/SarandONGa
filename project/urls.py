from django.urls import path
from . import views

urlpatterns = [
    path('create', views.project_create, name='project_create'),
    path('<int:project_id>', views.project_details, name='project_details'),
    path('<int:project_id>/delete',
         views.project_delete, name="project_delete"),
    path('<int:project_id>/update', views.project_update, name='project_update')
]

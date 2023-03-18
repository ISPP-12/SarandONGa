from django.urls import path
from . import views

urlpatterns = [
    path("home/list",views.home_list,name="home_list"),
    path("home/create",views.home_create,name="home_create"),
    path("home/delete",views.home_delete, name="home_delete")
]
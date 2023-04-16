from django.urls import path
from . import views

urlpatterns = [
    path("list",views.home_list,name="home_list"),
    path("create",views.home_create,name="home_create"),
    # path("<int:home_id>",views.home_details, name="home_details"),
    path("<int:home_id>/delete",views.home_delete, name="home_delete"),
    path("<int:home_id>/update",views.home_update,name="home_update"),

]

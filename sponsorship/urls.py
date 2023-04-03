from django.urls import path
from . import views

urlpatterns = [
    path("list", views.sponsorship_list, name="sponsorship_list"),
    path("create", views.sponsorship_create, name="sponsorship_create"),
    path("<slug:sponsorship_slug>/delete",
         views.sponsorship_delete, name="sponsorship_delete"),
    path("<int:sponsorship_id>", views.sponsorship_details,
         name="sponsorship_details"),
    path("<int:sponsorship_id>/update",
         views.sponsorship_edit, name="sponsorship_edit")
]

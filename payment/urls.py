from django.urls import path
from . import views

urlpatterns = [
    path('create', views.payment_create, name="payment_create"),
    # path('list', views.payment_list, name="payment_list"),
    path('<int:payment_id>/delete', views.payment_delete, name="payment_delete"),
    path('<int:payment_id>/update', views.payment_update, name="payment_update"),
    # path('<int:payment_id>', views.payment_details, name="payment_details"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('list', views.payment_list, name="payment_list"),
    path('create', views.payment_create, name="payment_create"),
    path('<int:payment_id>/update', views.payment_update, name="payment_update"),


]

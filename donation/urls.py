from django.urls import path
from . import views

urlpatterns = [
    path('list',views.donation_list, name='donation_list'),
    path('create', views.donation_create, name='donation_create'),
    path('<int:donation_id>/update', views.donation_update, name='donation_update'),
    path('<int:donation_id>/delete', views.donation_delete, name='donation_delete'),
]

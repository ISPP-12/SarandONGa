from django.urls import path
from . import views

urlpatterns = [
    path('create',views.service_create, name='service_create'),
    path('list',views.service_list, name='service_list'),
    path('update/<int:service_id>',views.service_update, name='service_update')
]
from django.urls import path
from . import views

urlpatterns = [
    path('create',views.service_create, name='service_create'),
    path('list',views.service_list, name='service_list')

]
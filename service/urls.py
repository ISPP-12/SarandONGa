from django.urls import path
from . import views

urlpatterns = [
    path('<int:service_id>/update', views.service_update, name='service_update'),
    path('create',views.service_create, name='service_create'),
    # path('list',views.service_list, name='service_list'),
    path('<int:service_id>/delete', views.service_delete, name="service_delete"),
    # path('<int:service_id>',views.service_details, name='service_details'),

]
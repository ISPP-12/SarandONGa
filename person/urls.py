from django.urls import path
from . import views

urlpatterns = [
    path('workers/',views.workers_list, name='workers_list'),
    path('worker/create', views.create_worker, name="worker"),
    path('asem_user/', views.asem_user, name="asem_user"),
    path('asem/asem_user_list', views.asem_user_list, name="asem_user_list"),
    path('godfather/list', views.godfather_list, name="godfather_list"),
    path('godfather/create', views.godfather_create, name="subsidy"),
    path('child/create', views.create_child, name="new_child"),
]

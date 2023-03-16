from django.urls import path
from . import views

urlpatterns = [
    path('child/list', views.child_list, name='child_list'),
    path('child/create', views.child_create, name="child_create"),
    path('asem/create', views.user_create, name="user_create"),
    path('asem/list',views.user_list, name='user_list'),
    path('worker/list',views.worker_list, name='worker_list'),
    path('worker/create', views.worker_create, name="worker_create"),
    path('godfather/list', views.godfather_list, name="godfather_list"),
    path('godfather/create', views.godfather_create, name="godfather_create"),
    path('volunteer/list',views.volunteer_list, name='volunteer_list'),
    path('volunteer/create', views.volunteer_create, name='volunteer_create')
]

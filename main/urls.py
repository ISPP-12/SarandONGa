from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('donations',views.donations_list, name='donations_list'),
    path('component',views.component, name='component')

]
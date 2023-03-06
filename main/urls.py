from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('grants/', views.grants_list, name='grants_list')
]
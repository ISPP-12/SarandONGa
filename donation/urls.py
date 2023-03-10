from django.urls import path
from . import views

urlpatterns = [
    path('',views.donations_list, name='donations_list')
]
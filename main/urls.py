from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('components/', views.components, name='components'),
    path('gateway/done/', views.payment_done, name='done'),
    path('gateway/canceled/', views.payment_canceled, name='canceled'),
    path('gateway/', views.payment_process, name='gateway'),
]

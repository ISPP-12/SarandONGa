from django.urls import path, include
from . import views
import donation.urls as donation_urls

urlpatterns = [
    path('', views.index, name='index'),
    path('donations/', include(donation_urls), name='donations'),
]
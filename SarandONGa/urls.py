"""SarandONGa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from subsidy import views as subsidy_views
from person import views as person_views
from service import views as service_views
from donation import urls as donation_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('subsidy/', subsidy_views.subsidy, name="subsidy"),
    path('asem_user/', person_views.asem_user, name="asem_user"),
    path('asem/asem_user_list', person_views.asem_user_list, name="asem_user_list"),
    path('donations/', include(donation_urls), name='donations'),
    path('subsidy/list', subsidy_views.subsidy_list, name="subsidy"),
    path('service/list', service_views.service_list, name="service_list")
]

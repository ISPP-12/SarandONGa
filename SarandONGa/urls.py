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
from payment import views as payment_views
from stock import views as stock_views
from service import views as service_views
from donation import urls as donation_urls
from person import urls as person_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('subsidy/', subsidy_views.subsidy, name="subsidy"),
    path('payment/create', payment_views.create_payment, name="donationNew"),
    path('stock/list', stock_views.stock_list, name="stock_list"),
    path('person/', include(person_urls), name='persons'),
    path('asem_user/', person_views.asem_user, name="asem_user"),
    path('asem/asem_user_list', person_views.asem_user_list, name="asem_user_list"),
    path('payment/list', payment_views.payment_list, name="payment_list"),
    path('donations/', include(donation_urls), name='donations'),
    path('subsidy/list', subsidy_views.subsidy_list, name="subsidy"),
    path('service/list', service_views.service_list, name="service_list")
    path('worker/create', person_views.create_worker, name="worker")

]

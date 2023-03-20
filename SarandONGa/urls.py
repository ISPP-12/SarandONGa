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
from main import views as main_views
from subsidy import urls as subsidy_urls
from stock import urls as stock_urls
from donation import urls as donation_urls
from payment import urls as payment_urls
from service import urls as service_urls
from person import urls as person_urls
from home import urls as home_urls
from sponsorship import urls as sponsorship_urls
from main import urls as main_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('subsidy/', include(subsidy_urls), name="subsidy"),
    path('donations/', include(donation_urls), name='donations'),
    path('subsidy/', include(subsidy_urls), name="subsidy"),
    path('stock/', include(stock_urls), name="stock"),
    path('donation/', include(donation_urls), name='donation'),
    path('user/', include(person_urls), name='user'),
    path('service/', include(service_urls),name="service"),
    path('home/',include(home_urls), name="home"),
    path('payment/',include(payment_urls), name="payment"),
    path('', main_views.index, name="index"),
    path('sponsorship/',include(sponsorship_urls), name="sponsorship"),

]

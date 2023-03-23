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
from subsidy import urls as subsidy_urls
from stock import urls as stock_urls
from donation import urls as donation_urls
from payment import urls as payment_urls
from service import urls as service_urls
from person import urls as person_urls
from payment import urls as payments_urls
from django.conf import settings
from django.conf.urls.static import static
from home import urls as home_urls
from sponsorship import urls as sponsorship_urls
from main import urls as main_urls
from proyect import urls as proyect_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('subsidy/', include(subsidy_urls), name="subsidy"),
    path('payment/', include(payment_urls), name="payment"),
    path('donations/', include(donation_urls), name='donations'),
    path('stock/', include(stock_urls), name="stock"),
    path('donation/', include(donation_urls), name='donation'),
    path('user/', include(person_urls), name='user'),
    path('service/', include(service_urls),name="service"),
    path('home/',include(home_urls), name="home"),
    path('payment/', include(payment_urls), name="payment"),
    path('', include(person_urls), name="person"),
    path('sponsorship/',include(sponsorship_urls), name="sponsorship"),
    path('proyect/',include(proyect_urls),name = "proyect"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

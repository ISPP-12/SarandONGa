from django.urls import path
from . import views

urlpatterns = [
    path('list', views.subsidy_list, name="subsidy_list"),
    path('create', views.subsidy_create, name="subsidy_create"),
    path('<int:subsidy_id>/delete/', views.subsidy_delete, name='subsidy_delete'),
]

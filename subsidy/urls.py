from django.urls import path
from . import views

urlpatterns = [
    path('list', views.subsidy_list, name="subsidy_list"),
    path('create', views.subsidy_create, name="subsidy_create"),
    path('<int:subsidy_id>/update', views.subsidy_update, name='subsidy_update'),
    path('<int:subsidy_id>/delete', views.subsidy_delete, name='subsidy_delete'),
    path('<int:subsidy_id>', views.subsidy_details, name='subsidy_details'),
    # path('<int:subsidy_id>/download_document', views.subsidy_download_document, name='download_document'),
]

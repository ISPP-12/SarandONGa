from django.urls import path
from . import views

urlpatterns = [
    path('child/list', views.child_list, name='child_list'),
    path('child/create', views.child_create, name="child_create"),
    path('child/<int:child_id>/update', views.child_update, name='child_update'),
    path('child/<int:child_id>', views.child_details, name="child_details"),
    path('child/<int:child_id>/delete', views.child_delete, name="child_delete"),
    path('asem/create', views.user_create, name="user_create"),
    path('asem/list', views.user_list, name='user_list'),
    path('asem/<int:asem_user_id>/delete',
         views.asem_user_delete, name='asem_user_delete'),
    path('asem/<int:asem_user_id>/update',
         views.user_update, name='user_update'),
    path('asem/<int:asem_user_id>',
         views.asem_user_details, name='asem_user_details'),
    path('worker/<int:worker_id>', views.worker_details, name='worker_details'),
    path('worker/list', views.worker_list, name="worker_list"),
    path('worker/create', views.worker_create, name="worker_create"),
    path('worker/<int:worker_id>', views.worker_details, name="worker_details"),
    path('worker/<int:worker_id>/update',
         views.worker_update, name='worker_update'),
    path('worker/<int:worker_id>/delete',
         views.worker_delete, name="worker_delete"),
    path('update_password/', views.UpdatePasswordView.as_view(),
         name='update_password'),
    path('godfather/list', views.godfather_list, name="godfather_list"),
    path('godfather/create', views.godfather_create, name="godfather_create"),
    path('godfather/<int:godfather_id>/update',
         views.godfather_update, name='godfather_update'),
    path('godfather/<int:godfather_id>',
         views.godfather_details, name="godfather_details"),
    path('godfather/<int:godfather_id>/delete',
         views.godfather_delete, name="godfather_delete"),
    path('volunteer/list', views.volunteer_list, name='volunteer_list'),
    path('volunteer/<int:volunteer_id>',
         views.volunteer_details, name='volunteer_details'),
    path('volunteer/create', views.volunteer_create, name='volunteer_create'),
    path('volunteer/<int:volunteer_id>/update',
         views.volunteer_update, name='volunteer_update'),
    path('volunteer/<int:volunteer_id>/delete',
         views.volunteer_delete, name='volunteer_delete'),
    path('api/child_age/', views.child_age, name='child_age'),
]

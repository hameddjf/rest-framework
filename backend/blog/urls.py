# import from django
from django.urls import path
# import from intenals app
from .views import (
    drf_views , 
    drf_detail , 
    drf_user_views , 
    drf_user_detail , 
    drf_delete_view , 
    drf_update_view , 
    drf_retrieve_view
)

app_name = 'blog'
urlpatterns = [
    path('', drf_views.as_view(), name='rest_views'),
    path('<int:pk>', drf_detail.as_view(), name='detail'),
    path('<slug:slug>', drf_detail.as_view(), name='detail_view'),

    path('<int:pk>/retrieve/', drf_retrieve_view.as_view(), name='retrieve_detail'),
    path('<slug:slug>/retrieve/', drf_retrieve_view.as_view(), name='retrieve_view'),


    path('<int:pk>/delete/', drf_delete_view.as_view(), name='delete_detail'),
    path('<slug:slug>/delete/', drf_delete_view.as_view(), name='delete_view'),

    path('<int:pk>/update/', drf_update_view.as_view(), name='update_detail'),
    path('<slug:slug>/update/', drf_update_view.as_view(), name='update_view'),


    path('users/', drf_user_views.as_view(), name='user_rest_views'),
    path('users/<int:pk>', drf_user_detail.as_view(), name='user_detail'),

    path('users//retrieve/', drf_retrieve_view.as_view(), name='user_rest_views'),
    path('users/<int:pk>/retrieve/', drf_retrieve_view.as_view(), name='user_detail'),

    path('users//delete/', drf_delete_view.as_view(), name='user_rest_views'),
    path('users/<int:pk>/delete/', drf_delete_view.as_view(), name='user_detail'),

    path('users//update/', drf_update_view.as_view(), name='user_rest_views'),
    path('users/<int:pk>/update/', drf_update_view.as_view(), name='user_detail'),
]

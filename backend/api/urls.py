# import from django
from django.urls import path
# import from intenals app
from .views import drf_views, drf_detail_view , drf_user_views , drf_detail_user_view


app_name = 'api'
urlpatterns = [
    path('', drf_views.as_view(), name='rest_views'),
    path('<int:pk>', drf_detail_view.as_view(), name='detail'),
    path('<slug:slug>', drf_detail_view.as_view(), name='detail_list'),

    path('users/', drf_user_views.as_view(), name='user_views'),
    path('users/<int:pk>', drf_detail_user_view.as_view(), name='user_detail'),

]

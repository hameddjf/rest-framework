"""
URL configuration for rest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# import from stl
from dj_rest_auth.views import PasswordResetConfirmView
# from rest_framework.authtoken.views import obtain_auth_token

# import from internal apps

from api.views import confimed_password
# from blog.views import revoketoken

urlpatterns = [
    path("admin/", admin.site.urls),

    path('', include('api.urls')),
    path('blog/', include('blog.urls')),

    path('blog/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('blog/dj-rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),

    path('blog/dj-rest-auth/password/reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path(
        r'^account-confirm-email/(?P<key>[-:\w]+)/$', confimed_password.as_view(),
        name='account_confirm_email',
    ),


    # path('blog/token-auth/', obtain_auth_token),
    # path('blog/revoke/', revoketoken.as_view()),

    # jost for session authentication
    # path('api-auth/', include('rest_framework.urls')),

]

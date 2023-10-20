# import from django
from django.contrib.auth.models import User
# from django.shortcuts import render
# import from internal apps
from api.models import drf_courses
from .serializers import drf_serializers , drf_user_serializers
from .permissions import IsSuperUser , IsOwnerOrReadOnly , IsStaffOrReadOnly , IsSuperuserOrOwnerReadOnly
# import from standard library
from rest_framework.generics import (
        ListAPIView ,  
        CreateAPIView ,
        ListCreateAPIView , 
        RetrieveAPIView , 
        DestroyAPIView , 
        RetrieveDestroyAPIView  , 
        UpdateAPIView , 
        RetrieveUpdateDestroyAPIView ,
    )
from rest_framework.permissions import IsAdminUser

class drf_retrieve_view(RetrieveAPIView):
    queryset = drf_courses.objects.all()
    serializer_class = drf_serializers

class drf_delete_view(DestroyAPIView):
    queryset = drf_courses.objects.all()
    serializer_class = drf_serializers

class drf_update_view(UpdateAPIView):
    queryset = drf_courses.objects.all()
    serializer_class = drf_serializers


class drf_views(ListCreateAPIView):
    queryset = drf_courses.objects.all()  # گرفتن اطلاعات ار مدل
    serializer_class = drf_serializers

class drf_detail(RetrieveUpdateDestroyAPIView):
    queryset = drf_courses.objects.all()  # گرفتن اطلاعات ار مدل
    serializer_class = drf_serializers
    permission_classes = (IsStaffOrReadOnly , IsOwnerOrReadOnly)
    # lookup_field = ('pk'or 'slug')

class drf_user_views(ListCreateAPIView):
    queryset = User.objects.all()  # گرفتن اطلاعات ار مدل
    serializer_class = drf_user_serializers
    permission_classes = (IsSuperuserOrOwnerReadOnly , ) # دسترسی فقط برای ادمین ها

class drf_user_detail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()  # گرفتن اطلاعات ار مدل
    serializer_class = drf_user_serializers
    permission_classes = (IsSuperuserOrOwnerReadOnly , ) # دسترسی فقط برای سوپریوزرها / استف هام میتونن فقط ببینن
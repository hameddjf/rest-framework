# import from django
from django.contrib.auth.models import User
# import from standard library
from rest_framework import serializers
# import from internal apps
from api.models import drf_courses


class drf_serializers(serializers.ModelSerializer):
    class Meta:
        model = drf_courses
        # fields = ('title', 'slug', 'author', 'content', 'publish', 'status')
        # exclude = ('created', 'updated')  # همه بجز اینا
        fields = '__all__'

class drf_user_serializers(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('title', 'slug', 'author', 'content', 'publish', 'status')
        # exclude = ('created', 'updated')  # همه بجز اینا
        fields = '__all__'


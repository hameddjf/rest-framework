# import from django
from django.contrib import admin
# import from intenals app
from .models import drf_courses
# Register your models here.

admin.site.register(drf_courses)

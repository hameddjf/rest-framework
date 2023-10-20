# import from django
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.contrib.auth.models import User
# import from intenals app
from .models import drf_courses

# Create your views here.


class drf_views(ListView):
    def get_queryset(self):
        return drf_courses.objects.filter(status=True)


class drf_detail_view(DetailView):
    def get_object(self):
        # کیبورد ارگیومنت/ پرایمری کی ایدی عددی مخصوص یک مقاله هستش
        return get_object_or_404(drf_courses.objects.filter(Q(pk=self.kwargs.get('pk')) | Q(slug=self.kwargs.get('slug')), status=True))
    # get_object_or_404 ابجکتیه ک میتونیم باش یسری چیزارو دور بزنیم .. اگ میخاستیم از گت استفاده کنیم مجبور ب کدزدن های بیشتر برای ارور و مشکلاتی ک ممکن بود پیش بیاد مینوشتیم ولی با این شورتکارت اینچیزارو دور میزنیم

class drf_user_views(ListView):
    def get_queryset(self):
        return User.objects.filter(status=True)


class drf_detail_user_view(DetailView):
    def get_object(self):
        # کیبورد ارگیومنت/ پرایمری کی ایدی عددی مخصوص یک مقاله هستش
        return get_object_or_404(User.objects.filter(is_superuser=True))
    # get_object_or_404 ابجکتیه ک میتونیم باش یسری چیزارو دور بزنیم .. اگ میخاستیم از گت استفاده کنیم مجبور ب کدزدن های بیشتر برای ارور و مشکلاتی ک ممکن بود پیش بیاد مینوشتیم ولی با این شورتکارت اینچیزارو دور میزنیم

from django.urls import path, re_path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='blog_index'),
    re_path(r'^(?P<blog_id>[0-9]+)', views.detail,name='blog_detail'),

]
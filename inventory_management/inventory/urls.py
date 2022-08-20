from django.urls import re_path
from .views import * 

urlpatterns = [
  re_path(r'^$', index, name='index'),
  re_path(r'^display_desktops$', display_desktops, name='display_desktops'),
  re_path(r'^display_laptops$', display_laptops, name='display_laptops'),
  re_path(r'^display_mobiles$', display_mobiles, name='display_mobiles'),
  re_path(r'^display_all$', display_all, name='display_all'),
]
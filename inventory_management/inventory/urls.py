from django.urls import re_path
from .views import * 

urlpatterns = [
  # Pages
  re_path(r'^$', index, name='index'),
  re_path(r'^about$', about, name='about'),

  # Table displays
  re_path(r'^display_desktops$', display_desktops, name='display_desktops'),
  re_path(r'^display_laptops$', display_laptops, name='display_laptops'),
  re_path(r'^display_mobiles$', display_mobiles, name='display_mobiles'),
  re_path(r'^display_all$', display_all, name='display_all'),

  # Forms
  re_path(r'^add_desktop$', add_desktop, name='add_desktop'),
  re_path(r'^add_laptop$', add_laptop, name='add_laptop'),
  re_path(r'^add_mobile$', add_mobile, name='add_mobile'),
]
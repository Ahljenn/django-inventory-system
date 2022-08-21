from django import forms
from .models import * 

class DesktopForm(forms.ModelForm):
  name = 'Desktop'
  class Meta:
    model = Desktop
    fields = ('type', 'issues', 'description', 'condition', 'status', 'price')

class LaptopForm(forms.ModelForm):
  name = 'Laptop'
  class Meta:
    model = Laptop
    fields = ('type', 'issues', 'description', 'condition', 'status', 'price')

class MobileForm(forms.ModelForm):
  name = 'Mobile'
  class Meta:
    model = Mobile
    fields = ('type', 'issues', 'description', 'condition', 'status', 'price')
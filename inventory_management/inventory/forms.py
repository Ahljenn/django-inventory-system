from django import forms
from .models import * 

class DesktopForm(forms.ModelForm):
  class Meta:
    model = Desktop
    fields = ('type', 'issues', 'description', 'condition', 'status', 'price')

class LaptopForm(forms.ModelForm):
  class Meta:
    model = Laptop
    fields = ('type', 'issues', 'description', 'condition', 'status', 'price')

class MobileForm(forms.ModelForm):
  class Meta:
    model = Mobile
    fields = ('type', 'issues', 'description', 'condition', 'status', 'price')
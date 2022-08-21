from django.shortcuts import render, redirect
from itertools import chain
from .models import *
from .forms import * 
# Views define the functions for each api end point
# Takes in HTTP request and returns a response (render)

# Create your views here.
def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def display_device(request, cls):
  items = cls.objects.all()
  context = {
    'items' : items,
    'header' : cls.name,
  }
  return render(request, 'index.html', context)

def display_desktops(request):
  return display_device(request, Desktop)

def display_laptops(request):
  return display_device(request, Laptop)

def display_mobiles(request):
  return display_device(request, Mobile)

def display_all(request):
  items = list(chain(Desktop.objects.all(), Laptop.objects.all(), Mobile.objects.all()))
  context = {
    'items' : items,
    'header' : 'All Items',
  }
  return render(request, 'index.html', context)

def add_device(request, cls):
  '''Modularized view to take in a class (cls) as a parameter
     Generalized function to prevent rewriting of the interface
  '''
  if request.method == 'POST':
    form = cls(request.POST)

    if form.is_valid():
      form.save()
      return redirect('index')
      
  else:
    # Otherwise, display form
    form = cls()
    return render(request, 'add_new.html', {
      'form': form, 
      'header': cls.name + ' Device'
      })

def add_desktop(request):
  return add_device(request, DesktopForm)

def add_laptop(request):
  return add_device(request, LaptopForm)

def add_mobile(request):
  return add_device(request, MobileForm)
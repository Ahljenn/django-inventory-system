from django.shortcuts import render
from itertools import chain
from .models import *
from .forms import * 
# Views define the functions for each api end point
# Takes in HTTP request and returns a response (render)

# Create your views here.
def index(request):
  return render(request, 'index.html')

def display_desktops(request):
  items = Desktop.objects.all()
  context = {
    'items' : items,
    'header' : 'Desktops',
  }
  return render(request, 'index.html', context)

def display_laptops(request):
  items = Laptop.objects.all()
  context = {
    'items' : items,
    'header' : 'Laptops',
  }
  return render(request, 'index.html', context)

def display_mobiles(request):
  items = Mobile.objects.all()
  context = {
    'items' : items,
    'header' : 'Mobiles',
  }
  return render(request, 'index.html', context)

def display_all(request):
  items = list(chain(Desktop.objects.all(), Laptop.objects.all(), Mobile.objects.all()))
  context = {
    'items' : items,
    'header' : 'All Items',
  }
  return render(request, 'index.html', context)

def add_desktop(request):
  if request.method == 'POST':
    form = DesktopForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect('index')
      
  else:
    # Otherwise, display form
    form = DesktopForm()
    return render(request, 'add_new.html', {'form': form})
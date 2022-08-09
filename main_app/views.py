from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Car, Mod
from .forms import  ServicesForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cars_index(request):
  cars = Car.objects.all()
  return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  services_form = ServicesForm()
  return render(request, 'cars/detail.html', {
    'car': car, 'services_form': services_form
  })

class CarCreate(CreateView):
  model = Car
  fields = '__all__'

class CarUpdate(UpdateView):
  model = Car
  fields = ['make', 'model', 'oiltype', 'year']

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'

def add_services(request, car_id):
  form = ServicesForm(request.POST)
  if form.is_valid():
    new_services = form.save(commit=False)
    new_services.car_id = car_id
    new_services.save()
  return redirect('cars_detail', car_id=car_id)

class ModCreate(CreateView):
  model = Mod
  fields = '__all__'

class ModList(ListView):
  model = Mod

class ModDetail(DetailView):
  model = Mod

class ModUpdate(UpdateView):
  model = Mod
  fields = ['name', 'color']

class ModDelete(DeleteView):
  model = Mod
  success_url = '/mods/'

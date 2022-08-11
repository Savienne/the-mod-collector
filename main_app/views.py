from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Car, Mod
from .forms import  ServicesForm

# Create your views here.
class home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def cars_index(request):
  cars = Car.objects.filter(user=request.user)
  return render(request, 'cars/index.html', { 'cars': cars })

@login_required
def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  mods_car_doesnt_have = Mod.objects.exclude(id__in = car.mods.all().values_list('id'))
  services_form = ServicesForm()
  return render(request, 'cars/detail.html', {
    'car': car, 'services_form': services_form, 'mods': mods_car_doesnt_have
  })

class CarCreate(LoginRequiredMixin, CreateView):
  model = Car
  fields = '__all__'

class CarUpdate(LoginRequiredMixin, UpdateView):
  model = Car
  fields = ['make', 'model', 'oiltype', 'year']

class CarDelete(LoginRequiredMixin, DeleteView):
  model = Car
  success_url = '/cars/'

@login_required
def add_services(request, car_id):
  form = ServicesForm(request.POST)
  if form.is_valid():
    new_services = form.save(commit=False)
    new_services.car_id = car_id
    new_services.save()
  return redirect('cars_detail', car_id=car_id)

class ModCreate(LoginRequiredMixin, CreateView):
  model = Mod
  fields = '__all__'

class ModList(LoginRequiredMixin, ListView):
  model = Mod

class ModDetail(LoginRequiredMixin, DetailView):
  model = Mod

class ModUpdate(LoginRequiredMixin, UpdateView):
  model = Mod
  fields = ['name', 'color']

class ModDelete(LoginRequiredMixin, DeleteView):
  model = Mod
  success_url = '/mods/'

@login_required
def assoc_mod(request, car_id, mod_id):
  Car.objects.get(id=car_id).mods.add(mod_id)
  return redirect('cars_detail', car_id=car_id)

def signup(request):
  error_message = ""
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cars_index')
    else:
      error_message = "Invalid sign up - try again"
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

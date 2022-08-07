from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car
from .forms import  ServiceForm

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
  feeding_form = ServiceForm()
  return render(request, 'cars/detail.html', {
    'car': car, 'feeding_form': feeding_form
  })

class CarCreate(CreateView):
  model = Car
  fields = '__all__'

class CarUpdate(UpdateView):
  model = Car
  fields = ['model', 'oiltype', 'year']

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'

def add_service(request, car_id):
  form = ServiceForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.car_id = car_id
    new_feeding.save()
  return redirect('cars_detail', car_id=car_id)
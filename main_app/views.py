from django.shortcuts import render
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Car:  # Note that parens are optional if not inheriting from another class
  def __init__(self, make, model, oiltype, year):
    self.make = make
    self.model = model
    self.oiltype = oiltype
    self.year = year

cars = [
  Car('Lolo', 'tabby', 'Kinda rude.', 3),
  Car('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  Car('Fancy', 'bombay', 'Happy fluff ball.', 4),
  Car('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Found My Dream Car</h1>')

def about(request):
  return render(request, 'about.html')

def cars_index(request):
  return render(request, 'cars/index.html', { 'cars': cars})


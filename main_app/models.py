from django.db import models
from django.urls import reverse

# Create your models here.

class Car(models.Model): 
  make = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  oiltype = models.TextField(max_length=250)
  year = models.IntegerField()

  def __str__(self):
    return self.make

  def get_absolute_url(self):
    return reverse('cars_detail', kwargs={'car_id': self.id})

MAINTENANCE = (
  ('A', '3 month service'),
  ('B', '6 month service'),
  ('C', '1 year service')
)

class Service(models.Model):
  date = models.DateField('Service date')
  maintenance = models.CharField(
    max_length=1,
    choices=MAINTENANCE,
    default=MAINTENANCE[0][0]
  )
  car = models.ForeignKey(Car, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_maintenance_display()} on {self.date}"

  class Meta:
    ordering = ['-date']
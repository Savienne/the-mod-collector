from django.db import models
from django.urls import reverse
from datetime import date
# from django.contrib.auth.models import User

SERVICES = (
  ('A', 'Three Month Service'),
  ('B', 'Six Month Service'),
  ('C', 'One Year Service')
)

# Create your models here.
class Mod(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("mods_detail", kwargs={"pk": self.id})

class Car(models.Model): 
  make = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  oiltype = models.TextField(max_length=250)
  year = models.IntegerField()
  # user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('cars_detail', kwargs={'car_id': self.id})

  def services_for_today(self):
    return self.services_set.filter(date=date.today()).count() >= len(SERVICES)

class Services(models.Model):
  date = models.DateField('Service date')
  maintenance = models.CharField(
    max_length=1,
    choices=SERVICES,
    default=SERVICES[0][0]
  )
  car = models.ForeignKey(Car, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_service_display()} on {self.date}"

  class Meta:
    ordering = ['-date']
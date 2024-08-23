from django.db import models
from django.core.validators import MinValueValidator

from airline.models import Airline

class Aircraft(models.Model):
    manufacturer_serial_number = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    operator_airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name='aircrafts')
    number_of_engines = models.IntegerField(validators= [MinValueValidator(1)])

    def __str__(self):
        return f"{self.model} ({self.manufacturer_serial_number})"

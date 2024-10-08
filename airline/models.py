from django.db import models

class Airline(models.Model):
    name = models.CharField(max_length=100)
    callsign = models.CharField(max_length=50)
    founded_year = models.IntegerField()
    base_airport = models.CharField(max_length=50)

    def __str__(self):
        return self.name


from django.contrib.auth.models import User
from django.core.validators import validate_comma_separated_integer_list
from django.db import models

# Create your models here.

class Sport(models.Model):
    name = models.CharField("Sport name", max_length=60)
    olsanka_id = models.IntegerField("ID in Olšanka hotel reservation system")

    def __str__(self):
        return self.name

class Reservation(models.Model):
    date = models.DateField("Desired date")
    window_from = models.TimeField("Beginning of the time window")
    window_to = models.TimeField("End of the time window for reservation")
    preferred_courts = models.TextField(validators=[validate_comma_separated_integer_list])
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

class Court(models.Model):
    olsanka_id = models.IntegerField("Court ID in Olšanka reservation system")
    name = models.CharField("Court name", max_length=60)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

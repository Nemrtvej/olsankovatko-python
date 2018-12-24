from django.contrib.auth.models import User
from django.core.validators import validate_comma_separated_integer_list
from django.db import models

# Create your models here.

class Reservation(models.Model):
    date = models.DateField("Desired date")
    window_from = models.TimeField("Beginning of the time window")
    window_to = models.TimeField("End of the time window for reservation")
    preferred_courts = models.TextField(validators=[validate_comma_separated_integer_list])
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
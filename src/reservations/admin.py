from django.contrib import admin

# Register your models here.
from .models import Reservation, Sport

admin.site.register(Reservation)
admin.site.register(Sport)
from django.contrib import admin

# Register your models here.
from .models import Court, Reservation, Sport

admin.site.register(Court)
admin.site.register(Reservation)
admin.site.register(Sport)
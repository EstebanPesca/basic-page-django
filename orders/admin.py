from django.contrib import admin
from .models import Order, LineOrder

# Register your models here.

admin.site.register([Order,LineOrder])

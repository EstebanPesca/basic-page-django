from django.contrib import admin
from .models import Service

# Register your models here.

# username: Admin
# address: admin@gmail.com
# admin1234

class serviceAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Service, serviceAdmin)
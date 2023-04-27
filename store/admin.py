from django.contrib import admin

from .models import Category_Product, Product, Size, Color

# Register your models here.


class productAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

admin.site.register(Product, productAdmin)
admin.site.register(Category_Product)
admin.site.register(Size)
admin.site.register(Color)

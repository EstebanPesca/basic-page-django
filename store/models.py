from django.db import models

# Create your models here.

class Size(models.Model):
    size = models.CharField(max_length=4)

    class Meta():
        verbose_name = 'size'
        verbose_name_plural = 'sizes'

    def __str__(self):
        return self.size

class Color(models.Model):
    name = models.CharField(max_length=20)

    class Meta():
        verbose_name = 'color'
        verbose_name_plural = 'colors'

    def __str__(self):
        return self.name

class Category_Product(models.Model):
    name = models.CharField(max_length=20)

    class Meta():
        verbose_name = 'CategoryProduct'
        verbose_name_plural = 'CategoriesProducts'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    disponibility = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category_Product)
    color = models.ManyToManyField(Color)
    size = models.ManyToManyField(Size)
    image = models.ImageField(upload_to="store", null=True,blank=True)
    price = models.FloatField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

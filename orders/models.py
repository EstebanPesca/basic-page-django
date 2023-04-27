from django.db import models
from django.contrib.auth import get_user_model
from store.models import Product
from django.db.models import F, Sum, FloatField

# Create your models here.

User = get_user_model()

class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
    
    @property
    def total(self):
        return self.lineorder_set.aggregate(
            total = Sum(F("price")*F("quantity"), Output_field=FloatField())
        )["total"]

    class Meta:
        db_table='orders'
        verbose_name='order'
        verbose_name_plural='orders'
        ordering = ['id']

    
class LineOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} units of {self.product.name}'
    
    class Meta:
        db_table='lineorder'
        verbose_name='line order'
        verbose_name_plural='lines orders'
        ordering = ['id']

from django.shortcuts import render
from .car import Car
from store.models import Product
from django.shortcuts import redirect

# Create your views here.

def add_product(request, product_id):

    car = Car(request)
    product = Product.objects.get(id=product_id)

    car.add(product=product)

    return redirect("Store")

def delete_product(request, product_id):

    car =Car(request)

    product = Product.objects.get(id=product_id)

    car.deleted(product)

    return redirect("Store")

def reduct_product(request, product_id):

    car =Car(request)

    product = Product.objects.get(id=product_id)

    car.reduct(product)

    return redirect("Store")

def clean_car(request):

    car =Car(request)

    car.clean_car()

    return redirect("Store")
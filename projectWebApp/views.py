from django.shortcuts import render, HttpResponse
from car.car import Car
from service.models import Service

# Create your views here.


def home(request):

    car = Car(request)

    return render(request, "ProjectWebApp/home.html")
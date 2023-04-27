from django.shortcuts import render

from service.models import Service

# Create your views here.

def service(request):

    services = Service.objects.all()

    return render(request, "services/service.html", {"services": services})
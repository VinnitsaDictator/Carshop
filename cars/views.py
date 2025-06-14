from django.shortcuts import render
from cars.models import Car
def index(request):
    return render(request, 'index.html')

def catalog(request):
    cars = Car.objects.all()
    return render(request, 'catalog.html',{'cars': cars})

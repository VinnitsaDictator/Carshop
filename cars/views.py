from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm
def index(request):
    return render(request, 'index.html')

def catalog(request):
    cars = Car.objects.all()
    return render(request, 'catalog.html',{'cars': cars})

def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog') 
    else:
        form = CarForm()
    return render(request, 'car_create.html', {'form': form})
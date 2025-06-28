from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm
from django.http import HttpResponse
from django.core.paginator import Paginator
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
def car_edit (request, id):
    try:
        car = Car.objects.get(id=id)
    except Car.DoesNotExist:
        return HttpResponse("Car not found")

    form = CarForm(instance=car)

    if request.method == "POST":
        form = CarForm(request.POST, request.FILES, instance=car)
        
        if form.is_valid():
            form.save()
            return redirect("catalog") 

    return render(request, "car_edit.html", {"form": form})
def car_list(request):
    car_list = Car.objects.all()
    paginator = Paginator(car_list, 5)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'car_list.html', context)
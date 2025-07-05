from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def catalog(request):
    cars = Car.objects.all()
    paginator = Paginator(cars, 5)  # 5 машин на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalog.html', {'page_obj': page_obj})

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

def favourite_list(request):
    favourite_ids = request.session.get('favourites', [])
    favourites = Car.objects.filter(id__in=favourite_ids)
    return render(request, 'favourite.html', {'favourites': favourites})

def add_to_favourite(request, car_id):
    favourites = request.session.get('favourites', [])
    if car_id not in favourites:
        favourites.append(car_id)
        request.session['favourites'] = favourites
    return redirect('favourite_list')

def remove_from_favourite(request, car_id):
    favourites = request.session.get('favourites', [])
    if car_id in favourites:
        favourites.remove(car_id)
        request.session['favourites'] = favourites
    return redirect('favourite_list')
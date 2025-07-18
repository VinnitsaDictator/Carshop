from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm, RentForm
from cars.models import Car, Rent
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def catalog(request):
    cars = Car.objects.all()
    car_status = {car.id: True for car in cars}
    paginator = Paginator(cars, 5)  # 5 машин на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalog.html', {'page_obj': page_obj, 'car_status': car_status})

def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
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

def rent_car(request):
    message = None
    if request.method == 'POST':
        form = RentForm(request.POST)
        if form.is_valid():
            car = form.cleaned_data['car']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            # Проверка занятости авто на выбранные даты
            overlap = Rent.objects.filter(car=car, end_date__gte=start_date, start_date__lte=end_date).exists()
            if overlap:
                message = 'Авто зайняте на вибрані дати!'
            else:
                form.save()
                return render(request, 'rentcar.html', {'form': RentForm(), 'success': True})
    else:
        form = RentForm()
    return render(request, 'rentcar.html', {'form': form, 'message': message})

def car_detail(request, id):
    car = Car.objects.get(id=id)
    return render(request, 'car_detail.html', {'car': car})
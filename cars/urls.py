"""
URL configuration for managercar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from cars import views



urlpatterns = [
    path('', views.index, name = 'index'),
    path('catalog/', views.catalog, name = 'catalog'),
    path('create/', views.car_create, name='car_create'),
    path('edit/<int:id>/', views.car_edit, name='car_edit'),
    path('favourites/', views.favourite_list, name='favourite_list'),
    path('favourites/add/<int:car_id>/', views.add_to_favourite, name='add_to_favourite'),
    path('favourites/remove/<int:car_id>/', views.remove_from_favourite, name='remove_from_favourite'),
    path('rent/', views.rent_car, name='rent_car'),
    path('car/<int:id>/', views.car_detail, name='car_detail'),
   
]

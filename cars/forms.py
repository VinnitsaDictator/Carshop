from django import forms
from cars.models import Car, Rent

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'name', 'year', 'price', 'image']

class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ['car', 'start_date', 'end_date', 'name', 'email', 'phone']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
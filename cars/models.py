from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.brand}{self.name}{self.year}"

class Rent(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='rents')
    start_date = models.DateField()
    end_date = models.DateField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.car} {self.start_date} - {self.end_date}"

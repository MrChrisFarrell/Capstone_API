from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)
    company_key = models.CharField(max_length=50, unique=True)
    photo_url = models.CharField(max_length=200, null=True)
    details = models.CharField(max_length=500)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=10)
    owner = models.CharField(max_length=20)


class Promotion(models.Model):
    company = models.ForeignKey(Company, related_name='promotion', on_delete=models.CASCADE)
    details = models.CharField(max_length=200)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    photo_url = models.CharField(max_length=200, null=True)


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    email = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.IntegerField(default=0)


class CompanyLatLong(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)

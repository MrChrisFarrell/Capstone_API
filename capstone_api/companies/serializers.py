from rest_framework import serializers
from .models import Company, Promotion, Employee, CompanyLatLong, EmployeeLatLong


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'company_key', 'photo_url', 'details', 'street_address', 'city', 'state', 'zip_code', 'phone_number', 'owner']


class PromotionGetSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Promotion
        fields = ['id', 'company', 'details', 'start_date', 'end_date', 'photo_url']


class PromotionPPDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['id', 'company', 'details', 'start_date', 'end_date', 'photo_url']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'street_address', 'city', 'state', 'zip_code', 'email', 'company', 'user']


class CompanyGetLatLongSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = CompanyLatLong
        fields = ['id', 'company', 'lat', 'long']


class CompanyPPDLatLongSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyLatLong
        fields = ['id', 'company', 'lat', 'long']


class EmployeeGetLatLongSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = EmployeeLatLong
        fields = ['id', 'employee', 'lat', 'long']


class EmployeePPDLatLongSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeLatLong
        fields = ['id', 'employee', 'lat', 'long']
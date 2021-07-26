from rest_framework import serializers
from .models import Company, Promotion, Employee


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'company_key', 'photo_url', 'details', 'street_address', 'city', 'state', 'zip_code', 'phone_number']


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['id', 'company', 'details', 'start_date', 'end_date', 'photo_url']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'street_address', 'city', 'state', 'zip_code', 'email', 'company']

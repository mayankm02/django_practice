from rest_framework import serializers
from myapp.models import Company, Employee

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Company
        fields="__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Employee
        fields="__all__"
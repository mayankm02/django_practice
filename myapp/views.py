from django.shortcuts import render
from rest_framework import viewsets
from myapp.models import Company, Employee
from myapp.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

    # for custom api
    # companies/{company_id}/employees
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=True):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company = company)
            emps_serializer = EmployeeSerializer(emps, many=True, context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({'message':'Company not exists.'})

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
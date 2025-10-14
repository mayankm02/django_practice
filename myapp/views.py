from django.shortcuts import render
from rest_framework import viewsets
from myapp.models import Company
from myapp.serializers import CompanySerializer
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

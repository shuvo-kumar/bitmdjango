from django.shortcuts import render
from django.views.generic import *
from rest_framework import viewsets
from restapp.models import EmployeeInfo
from restapp.serializers import EmployeeSerializer 

# Create your views here.
class HomeView (TemplateView):
    template_name = 'index.html'

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = EmployeeInfo.objects.all()
    serializer_class = EmployeeSerializer
    
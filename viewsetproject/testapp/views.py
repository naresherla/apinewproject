from django.shortcuts import render
from testapp.models import Employee
from rest_framework.viewsets import ModelViewSet
from testapp.serializers import Employeeserializer
class viewsetcrudview(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer

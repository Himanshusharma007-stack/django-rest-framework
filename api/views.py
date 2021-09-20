from django.shortcuts import render
from .serializers import AddressSerializer, StudentSerializer
from rest_framework import viewsets
from .models import Student, Address

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class= StudentSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset= Address.objects.all()
    serializer_class= AddressSerializer
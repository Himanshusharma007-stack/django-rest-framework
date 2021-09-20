from .models import Address, Student 
from rest_framework import serializers

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model= Address
        fields= ['id', 'city', 'landmark', 'postal_address', 'student']

class StudentSerializer(serializers.ModelSerializer):
    address= AddressSerializer(many = True, read_only= True)
    class Meta:
        model= Student
        fields= ['id', 'student_name', 'standard', 'address']
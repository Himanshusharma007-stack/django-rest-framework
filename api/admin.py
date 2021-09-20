from django.contrib import admin
from .models import Student, Address

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display= ['id', 'student_name', 'standard']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display= ['id', 'city', 'landmark', 'postal_address', 'student']
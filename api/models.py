from django.db import models

# Create your models here.
class Student(models.Model):
    student_name= models.CharField(max_length=25)
    standard= models.IntegerField()

    def __str__(self):
        return self.student_name

class Address(models.Model):
    city = models.CharField(max_length=20)
    landmark = models.CharField(max_length=100)
    student= models.ForeignKey(Student, on_delete=models.CASCADE, related_name='address')
    postal_address= models.CharField(max_length=100)

    def __str__(self):
        return self.city
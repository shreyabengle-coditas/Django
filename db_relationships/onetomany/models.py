from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed

    def __str__(self):
        return self.name

class Address(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    # Add other fields as needed

    def __str__(self):
        return f"{self.street}, {self.city}"
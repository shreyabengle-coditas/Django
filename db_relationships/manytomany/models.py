from django.db import models

# Create your models here.
# models.py

from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    addresses = models.ManyToManyField('Address', related_name='employees')

    def __str__(self):
        return self.name

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.city}"

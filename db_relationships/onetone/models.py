from django.db import models

# Create your models h
class Address(models.Model):
    city=models.CharField(max_length=30)
    pincode = models.CharField(max_length=30)

    def __str__(self) -> str:
        return "City:" +self.city+"with Pincode:"+self.pincode

class Employee(models.Model):
    empid=models.CharField(max_length=10)
    empname=models.CharField(max_length=50)
    salary=models.CharField(max_length=30,default=0)
    address= models.OneToOneField(Address,on_delete=models.CASCADE,related_name="address_shreya")

    def __str__(self):
        return "[Empid:"+self.empid+"Ename:"+self.empname+"salary:"+self.salary+"address:"+self.address
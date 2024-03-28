from django.db import models

# Create your models here.
class Student(models.Model):
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    dob = models.DateField()
    # image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.f_name + " "+ self.l_name+" "+str(self.dob)

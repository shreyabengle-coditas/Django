from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    salary = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + " "+ self.last_name
    

class Teacher(models.Model):
    teacher_id = models.IntegerField()
    teacher_name = models.CharField(max_length=30)
    teacher_last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.teacher_id + " "+ self.teacher_name



from django.db import models
from datetime import datetime, time

# Create your models here.
class Student(models.Model):
    #choise field
    GENDER_CHOICES = [('Male', 'Male'),('Femail', 'Femail'),]

    name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True,blank = True, null = True)
    dob= models.DateField(default=datetime.now,blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Mail')
    
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.email} {self.gender}'
from django.db import models

# Create your models here.
class EmployeeInfo (models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Empolyee Name',max_length =100)
    email = models.CharField('Email Address',max_length =100)
    def __str__(self):
        return self.name
    
    

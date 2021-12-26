from django.db import models
from django.utils import timezone

# Create your models here.
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Department Name',max_length=100)
    
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Employee Name',max_length=100)
    email = models.EmailField(max_length=100,null=True,blank=True,verbose_name=('Email Address'))
    dob = models.DateField('Birth Date',default=timezone.now,blank=True,help_text='format:yyyy-mm-dd')
    salary = models.DecimalField('Monthly Salary',max_digits = 8,decimal_places=2,blank=True,null=True)
    photo = models.FileField(upload_to = "empimage",default = "empimage/blank.png",blank=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/"
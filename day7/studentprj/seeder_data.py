import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studentprj.settings')

import django
django.setup()

from studentapp.models import Student
from faker import Faker

fakezen = Faker()
def addstudent():
    fname = fakezen.name()
    femail = fakezen.email()
    fdob = fakezen.date()
    fmale = 'Male'
    
    std = Student.objects.get_or_create(name = fname,email = femail,dob=fdob, gender = fmale)[0]
    return std
    
def populate_data(n=10):
    for x in range(n):
        std = addstudent()
        
        
if __name__ == '__main__':
    print('Populating Data Please Wait.............')
    print('#' *50)
    populate_data(30)
    print('Populating Data Completed')
    print('#' *50)
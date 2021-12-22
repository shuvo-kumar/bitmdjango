import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studentprj.settings')

import django
django.setup()

from studentapp.models import Student
from django.contrib.auth.models import User
from django.contrib.auth.hashers  import make_password
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
    populate_data(10)
    print('Populating Data Completed')
    print('#' *50)
    
    user = User.objects.get_or_create(username = 'Shuvo', 
                                      password = make_password('pass1234'),
                                      email = 'shuvo@g.com', first_name ='Sabysachi', 
                                      last_name = 'Halder', 
                                      is_staff = True, 
                                      is_superuser = True, 
                                      is_active = True)
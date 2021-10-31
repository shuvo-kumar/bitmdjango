from django.shortcuts import render

# Create your views here.

def list (request):
    # variable
    students =[
        {'id': 1, 'name':'shuvo', 'email':'shuvo2email@gmail.com', 'dob':'2000-01-02', 'gender': 'Male' },
        {'id': 2, 'name':'Aramn', 'email':'aramn@gmail.com', 'dob':'1900-01-02', 'gender': 'Male' },
        {'id': 3, 'name':'Maruf', 'email':'shuvo2email@gmail.com', 'dob':'2001-01-02', 'gender': 'Male' },
        {'id': 4, 'name':'Arena', 'email':'shuvo2email@gmail.com', 'dob':'1922-01-02', 'gender': 'Femele' },
        {'id': 5, 'name':'sabyasachi halder', 'email':'shuvo2email@gmail.com', 'dob':'2021-01-02', 'gender': 'Male' },
        {'id': 6, 'name':'Tania', 'email':'shuvo2email@gmail.com', 'dob':'1982-01-02', 'gender': 'Femele' },
        {'id': 7, 'name':'Gulsan', 'email':'shuvo2email@gmail.com', 'dob':'1988-01-02', 'gender': 'Femele' },
        {'id': 8, 'name':'Rajbonshi', 'email':'shuvo2email@gmail.com', 'dob':'1955-01-02', 'gender': 'Male' },
        {'id': 9, 'name':'Rahim', 'email':'shuvo2email@gmail.com', 'dob':'1922-01-02', 'gender': 'Male' },
        {'id': 10, 'name':'Karim', 'email':'shuvo2email@gmail.com', 'dob':'1952-01-02', 'gender': 'Male' },
        {'id': 11, 'name':'shila ', 'email':'shuvo2email@gmail.com', 'dob':'1955-01-02', 'gender': 'Femele' },
        {'id': 12, 'name':'Mila', 'email':'shuvo2email@gmail.com', 'dob':'1954-01-02', 'gender': 'Femele' },
        {'id': 13, 'name':'Tila', 'email':'shuvo2email@gmail.com', 'dob':'1954-01-02', 'gender': 'Male' },
        {'id': 14, 'name':'Abul', 'email':'shuvo2email@gmail.com', 'dob':'1985-01-02', 'gender': 'Male' },
    ]


    contex = {'title':'List of Students', 'students':students}
    return render(request,'list.html', contex)
    # render () > html
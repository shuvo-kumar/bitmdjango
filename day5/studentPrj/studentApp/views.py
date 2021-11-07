from django.shortcuts import render
# 
from studentApp.models import Student


# Create your views here.


# new

def home(request):
    context ={'title':'Amar Djano shikhtei hobea'}
    return render (request,'stud/home.html',context)

def list(request):
    students = Student.objects.all()
    contex = {'title': 'Student List', 'students' : students}
    return render(request,'stud/list.html',contex)
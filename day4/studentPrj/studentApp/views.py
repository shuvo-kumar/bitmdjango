from django.shortcuts import render
from studentPrj.studentApp.models import Student

# Create your views here.


# new

def home(request):
    context ={'title':'Amar Djano shikhtei hobea'}
    return render (request,'stud/home.html',context)

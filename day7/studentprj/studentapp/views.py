from django.shortcuts import render

from studentapp.models import Student

# Create your views here.
def home(request):
    context = {'title':'Amar django siltai hobe'}
    return render(request, 'stud/home.html', context)

def list(request):
    students = Student.objects.order_by('-id')
    context = {'title ' : 'Student List', 'students': students}
    return render(request, 'stud/list.html',context)

    
def about(request):
    context = {'title': 'About'}
    return render(request, 'stud/about.html', context)
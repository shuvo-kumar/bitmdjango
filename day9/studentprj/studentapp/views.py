import django
from django.core import paginator
from django.shortcuts import redirect, render

from studentapp.models import Student
from django.core.paginator import Paginator

from .forms import StudentForm
from django.contrib import messages


# Create your views here.
def home(request):
    context = {'title':'Amar django siltai hobe'}
    return render(request, 'stud/home.html', context)

def list(request):
    std = Student.objects.order_by('-id')
    # std = Student.objects.all()
    std_list = std
    paginator = Paginator(std_list,10)
    
    page = request.GET.get('page')
    std = paginator.get_page(page)
    
    context = {'title ' : 'Student List', 'students': std}
    return render(request, 'stud/list.html',context)

    
def about(request):
    context = {'title': 'About'}
    return render(request, 'stud/about.html', context)

def create(request):
    # POST =when submit 
    # GET =befor submit
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Inserted Succesfully !')
            return redirect('list')
    else :
        form = StudentForm()     
        
    context = {'title' : 'Create Student', 'form':form}
    return render(request, 'stud/create.html',context,)
    
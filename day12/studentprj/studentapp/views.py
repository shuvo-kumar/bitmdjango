import django
from django.core import paginator
from django.shortcuts import redirect, render

from studentapp.models import Student
from django.core.paginator import Paginator

from .forms import StudentForm,SignUpForm
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
    return render(request, 'stud/create.html',context)

def details(request, id):
    student = Student.objects.get(pk = id)
    form = StudentForm(request.POST or None, instance=student)
    
    context = {'title' : 'Student Details', 'form':form, 'student':student}
    return render(request, 'stud/view.html',context)
        
def edit(request, id):
    if request.method == "POST":
        student = Student.objects.get(pk = id)
        form = StudentForm(request.POST or None, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Updated Succesfully !')
            return redirect('list')
    else:
        student = Student.objects.get(pk = id)
        form = StudentForm(request.POST or None, instance=student)
        
    context = {'title' : 'Edit Student ', 'form':form}
    return render(request, 'stud/create.html',context)

def delete(request, id):
    student = Student.objects.get(pk = id)
    student.delete()
    messages.success(request,'Data Delete Succesfully !')
    return redirect('list')

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            messages.success(request,'User create Succesfully !')
            return redirect('home')
    else :
        form = SignUpForm()     
    context = {'title' : 'Register User ', 'form':form}
    return render(request, 'registration/register.html',context)
        
        
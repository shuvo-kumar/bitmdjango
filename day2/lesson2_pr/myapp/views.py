from typing import ContextManager
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myview1(request):
    return HttpResponse('Hello World')


def welcome(request,name):
    return HttpResponse(f'Hello My Dear Friend {name}')
    
def show(request):
    context = {'tile' : 'Welcome'}
    return render(request,'home.htm',context) 
    # variable> context:dictionary>
    # returen rander() method with home.html


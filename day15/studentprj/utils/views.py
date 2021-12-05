
from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from .forms import EmailForm

from django.http import HttpResponse
from studentapp.models import Student
import csv 

# Create your views here.

def sent_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            varsubject = form.cleaned_data['subject']
            varmessage = form.cleaned_data['message']
            varemail = form.cleaned_data['email']
            
            varmail =EmailMessage(varsubject,varmessage,settings.EMAIL_HOST_USER,[varemail])
            
            # attach file here !
            if request.FILES :
                varFiles = request.FILES.getlist('attach')
                for f in varFiles:
                    varmail.attach(f.name,f.read(),f.content_type)
            # end of attach config
            
            varmail.send()
            messages.success(request,'Email Sent Successfuly !')
            return redirect('/')
    else:
        form = EmailForm()
            
        # context ={'form':form}    
    return render(request,'email/emailform.html',{'form':form})
                   
def export_csv(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment;filename= "student.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Id', 'Student Name', 'Email Address', 'Birth Date', 'Gender']) 
    students = Student.objects.all().values_list('id', 'name', 'email', 'dob', 'gender')
    
    
    for std in students:
        writer.writerow(std)
    
    return response
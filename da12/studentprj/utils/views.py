from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from .forms import EmailForm

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
                   
    
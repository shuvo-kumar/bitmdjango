from django import forms
from django.forms import fields
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentForm (forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        
        labels = {'dob': 'Date of Birth',}    
        
        
class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(required=False,max_length=100)
    last_name = forms.CharField(required=False,max_length=100)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email','password1', 'password2',)
    
    
    
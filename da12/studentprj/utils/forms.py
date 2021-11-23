from django import forms

class EmailForm (forms.Form):
    email = forms.EmailField(max_length=100, widget=forms.TextInput())
    subject = forms.CharField(max_length=100, widget=forms.TextInput())
    message = forms.CharField(max_length=100, widget=forms.TextArea(),label=(''))
    attach = forms.FileField(required=False,widget=forms.ClearableFileInput(attrs={'multiple':True}))
    
    

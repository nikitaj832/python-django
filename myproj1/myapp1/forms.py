from django import forms
from .models import student_details


# class student_forms():






class myform(forms.Form):
    
    
    name = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()




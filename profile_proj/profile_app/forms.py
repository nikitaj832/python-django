from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class profile_form(forms.Form):
    name=forms.CharField(required=True,widget=forms.TextInput(attrs=
    {'class': 'form.control','placeholder':'Enter your name'}))
    father_name=forms.CharField(required=True,widget=forms.TextInput(attrs=
    {'class': 'form.control','placeholder':'Enter your father name'}))
    mother_name=forms.CharField(required=True,widget=forms.TextInput(attrs=
    {'class': 'form.control','placeholder':'Enter your mother name'}))
    email=forms.EmailField(required=True,widget=forms.EmailInput(attrs=
    {'class': 'form.control','placeholder':'Enter your email'}))
    roll_no=forms.IntegerField(required=True,widget=forms.TextInput(attrs=
    {'class': 'form.control','placeholder':'Enter your roll no'}))
    stream=forms.CharField(required=True,widget=forms.TextInput(attrs=
    {'class': 'form.control','placeholder':'Enter your stream'}))
    address=forms.CharField(required=True,widget=forms.TextInput(attrs=
    {'class': 'form.control','placeholder':'address'}))
    state=forms.CharField(required=True,widget=forms.TextInput(attrs=
    {'class': 'form.control','placeholder':'state'}))
    city=forms.CharField(required=True,widget=forms.TextInput(attrs=
    {'class': 'form.control','placeholder':'city'}))
    pin_code=forms.CharField(required=True,widget=forms.TextInput(attrs=
    {'class': 'form.control','placeholder':'pin code'}))
    gender=forms.CharField(required=True,widget=forms.TextInput(attrs=
    {'class': 'form.control','placeholder':'gender'}))
    mobile_no=forms.CharField(required=True,widget=forms.TextInput(attrs=
    {'class': 'form.control','placeholder':'mobile no'}))
    image=forms.ImageField(required=True,widget=forms.FileInput(attrs=
    {'class': 'form.control','placeholder':'Enter your name'}))
    description=forms.CharField(required=True,widget=forms.TextInput(attrs=
    {'class': 'form.control','placeholder':'description'}))
    
    
    
class register(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email']
from django import forms
from .models import resume

# class resume_form(forms.Form):
#     name=forms.CharField(required=True,widget=forms.TextInput(attrs=
#     {'class': 'form.control','placeholder':'Enter your name'}))
#     date_of_birth = forms.DateField(required=True,widget=forms.TextInput(attrs=
#     {'class': 'form.control','placeholder':'Enter your date of birth'}))
#     post = forms.CharField(required=True,widget=forms.TextInput(attrs=
#     {'class': 'form.control','placeholder':'Post'}))
#     email=forms.EmailField(required=True,widget=forms.EmailInput(attrs=
#     {'class': 'form.control','placeholder':'Enter your email'}))
#     address = forms.CharField(required=True,widget=forms.TextInput(attrs=
#     {'class': 'form.control','placeholder':'Enter your address'}))
#     mobile_no=forms.CharField(required=True,widget=forms.TextInput(attrs=
#     {'class': 'form.control','placeholder':'mobile no'}))
#     linked_in =forms.CharField(required=True,widget=forms.TextInput(attrs=
#     {'class': 'form.control','placeholder':'linked id'}))
#     skills=forms.CharField(required=True,widget=forms.TextInput(attrs=
#     {'class': 'form.control','placeholder':'skills'}))
#     description=forms.CharField(required=True,widget=forms.TextInput(attrs=
#     {'class': 'form.control','placeholder':'description'}))
#     interest=forms.CharField(required=True,widget=forms.TextInput(attrs=
#     {'class': 'form.control','placeholder':'interest'}))
#     education=forms.CharField(required=True,widget=forms.TextInput(attrs=
#     {'class': 'form.control','placeholder':'education'}))
#     image=forms.ImageField(required=True,widget=forms.FileInput(attrs=
#     {'class': 'form.control','placeholder':'Enter your name'}))
#     experience=forms.CharField(required=True,widget=forms.TextInput(attrs=
#     {'class': 'form.control','placeholder':'experience'}))
#     language=forms.CharField(required=True,widget=forms.TextInput(attrs=
#     {'class': 'form.control','placeholder':'language'}))
#     git=forms.CharField(required=True,widget=forms.TextInput(attrs=
#     {'class': 'form.control','placeholder':'git id'}))



class resume_form(forms.ModelForm):
    class Meta:
        
        model = resume
        fields = ('__all__')
        # widget ={
        #     'name':forms.TextInput(attrs={'class':'form-control'})
        # }
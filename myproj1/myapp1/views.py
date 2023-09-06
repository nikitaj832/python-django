from django.shortcuts import render,HttpResponse
from .models import student_details
# Create your views here.


def index(request):
    return render(request,'index.html')


def contact(request):
    return render(request,'contact.html')

def index1(request):
    return render(request,'index1.html')

def forms(request):
    return render(request,'forms.html')

def index2(request):
    data = student_details.objects.all()
    for i in data:
        print(i)
    print(data)
    context= {
        'd':data
    }
    
    return render(request,'index2.html',context)   
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'index.html')


def position(request):
    return render(request,'position.html')

def home(request):
    return render(request,'home.html')

def catering(request):
    return render(request,'catering.html')


def transition(request):
    return render(request,'transition.html')
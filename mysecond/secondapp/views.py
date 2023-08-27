from django.shortcuts import render

# Create your views here.
def webpg(request):
    return render(request,'webpg.html')
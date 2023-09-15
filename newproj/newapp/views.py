from django.shortcuts import render,HttpResponse
from .models import resume
# # Create your views here.
from .forms import resume_form

# def resume(request):
#     return render(request,'resume.html')

def resumeform(request):
      if request.method== "POST":
          a =resume_form(request.POST,request.FILES)
          print(a)
        
          if a.is_valid():
            
            # name = a.cleaned_data['name']
            # date_of_birth = a.cleaned_data['date_of_birth']
            # post= a.cleaned_data['post']
            # email = a.cleaned_data['email']
            # mobile_no = a.cleaned_data['mobile_no']
            # linked_in = a.cleaned_data['linked_in']
            # address =a.cleaned_data['address']
            # interest =a.cleaned_data['interest']
            # experience =a.cleaned_data['experience']
            # language= a.cleaned_data['language']
            # skills =a.cleaned_data['skills']
            # education =a.cleaned_data['education']
            # image=a.cleaned_data['image']
            # description =a.cleaned_data['description']
            # git = a.cleaned_data['git']
            # myresume(name=name,date_of_birth=date_of_birth,post=post,email=email,linked_in=linked_in,skills=skills,address = address,interest=interest,experience= experience,language=language,mobile_no = mobile_no,image = image,description = description,education=education,git=git).save()
            
            a.save()
            return HttpResponse('Data saved !!!')
        
      a =resume_form()
      context={
        'a':a
      }
      return render(request,'forms.html',context)        
    
    
# def get_data(request):
#     data= resume.objects.all()
#     print(data)


def get_data(request):
    data= resume.objects.all()

    context ={
        'data':data
      
        
    }
    return render(request,'resume.html',context)    
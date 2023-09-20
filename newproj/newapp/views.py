from django.shortcuts import render,HttpResponse,redirect
from .models import resume 
# # Create your views here.
from .forms import resume_form,register_form
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout

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
            return redirect('/get/')
          
  
      a =resume_form()
      context={
        'a':a
      }
      return render(request,'forms.html',context)        
    
    
# def get_data(request):
#     data= resume.objects.all()
#     print(data)


def get_data(request):
    data= resume.objects.filter(user=request.user)
    skill = []
    skill_per = []
    interest = []
    language = []
    
    for i in data[0].skill_1.split(','):
      skill.append(i)
      
    print(skill)
    
    for i in data[0].percent_1.split(','):
      skill_per.append(i)
      
     
    for i in data[0].interest_1.split(','):
      interest.append(i)
    
         
    for i in data[0].language_1.split(','):
      language.append(i)
      
    print(skill_per)
    
    context = {
      
       'data':data,
       'skill':skill,
       'skill_per':skill_per,
       'interest':interest,
       'language':language
    }
     

    return render(request,'resume.html',context)    
  
  
def create_account(request):
  if request.method == 'POST':
    x= register_form(request.POST)
    if x.is_valid():
      x.save()
      return HttpResponse('data saved !!!')
    
  x = register_form()
  my_dict = {
    'x':x
  }
  
  return render(request,'auth_forms.html',my_dict)


def login_form(request):
  if request.method == 'POST':
     x= AuthenticationForm(data = request.POST)
     print('>>>>x',x)
     if x.is_valid():
       uname = x.cleaned_data['username']
       passw = x.cleaned_data['password']
       user = authenticate(username = uname, password = passw)
      
       if user is not None:
        login(request,user)
        return redirect('/resume_form/')
    
  x = AuthenticationForm()
  context = {
    'x':x
  }
  
  return render(request,'login_form.html',context)

def get_out(request):
  logout(request)
  return redirect('/login/')


def Create_account(request):
   
  if request.method == "POST":
    uname = request.POST.get('username')
    email = request.POST.get('email')
    passw = request.POST.get('password')
    print(uname,email,passw)
        
    if User.objects.filter(username=uname).first():
      messages.success(request,'username is taken')

    if User.objects.filter(email=email).first():
      messages.success(request,'email is taken')
              
    else:
      user = User(username=uname,email=email)
      user.set_password(passw)
      user.save()
      messages.success(request,'Account created !!')
  return render(request,'create_account.html')


def login_handle(request):
  
  if request.method == "POST":
    username = request.POST.get('username')
    password =request.POST.get('password')
    print(username,password)
         
    if not username or not password:
      messages.success(request,'Boths fields are required !')
    user_obj = User.objects.filter(username=username).first()
    user = authenticate(username=username,password=password)
    if user_obj is None:
      messages.success(request,'User Not found !')
    print(user_obj)
    if user is not None:
      login(request,user)
      return redirect('/resume_form/')
            
    if user is None:
      messages.success(request,'Wrong Password !!')
          
  
  return render(request,'Login.html')



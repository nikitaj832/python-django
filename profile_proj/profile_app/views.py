# from django.shortcuts import render,HttpResponse
# from .models import myprofile
# from .forms import myform

# # Create your views here.


# # def profile(request):
# #     if request.method == "POST":
# #         name= request.POST['name']
# #         f_name= request.POST['father_name']
# #         m_name= request.POST['mother_name']
# #         email= request.POST['email']
# #         r_no= request.POST['roll_no']
# #         stream= request.POST['stream']
# #         ad= request.POST['address']
# #         state= request.POST['state']
# #         c= request.POST['city']
# #         p= request.POST['pin_code']
# #         g= request.POST['gender']
# #         m= request.POST['mobile_no']
# #         i= request.POST['image']
# #         d= request.POST['description']
# #         myprofile(name=name, father_name=f_name, mother_name=m_name, email=email, roll_no=r_no, stream=stream, address=ad, state=state, city=c, pin_code=p, gender=g, mobile_no=m, image=i, description=d).save()
# #         print(name,f_name,m_name,email,r_no,stream,ad,state,c,p,g,m,i,d)

 
# #     return render(request,'profile.html')

    
    
# # def profileform(request):
# #     a = myform()
# #     context ={
# #     'a':a
# #      }
# #     return render(request,'forms.html',context)


# def profileform(request):
    
#     if request.method == "POST":
#         a= myform(request.POST,request.FILES)
#         print(a) 
        
#         if a.is_valid():
#           name =    a.cleaned_data['name']                               
#           father_name =a.cleaned_data['father_name']
#           mother_name = a.cleaned_data['mother_name']
#           email = a.cleaned_data['email']
#           roll_no =a.cleaned_data['roll_no']
#           stream = a.cleaned_data['stream']
#           address = a.cleaned_data['address']
#           state =  a.cleaned_data['state']
#           city     = a.cleaned_data['city']
#           pin_code  =a.cleaned_data['pin_code']
#           gender    =  a.cleaned_data['gender']
#           mobile_no =a.cleaned_data['mobile_no']
#           image  = a.cleaned_data['image']
#           description = a.cleaned_data['description']
           
#           myprofile(name=name, father_name=father_name, mother_name=mmother_name, email=email, roll_no=roll_no, stream=stream, address=address, state=state, city=city, pin_code=pin_code, gender=gender, mobile_no=mobile_no, image=image, description=description).save()
          

  
#         return HttpResponse('Data Saved !!!')
#     a = myform()
#     context ={
#         'a':a
#     }
#     return render(request,'forms.html',context)

   
from django.shortcuts import render,HttpResponse
from .models import myprofile
# Create your views here.
from .forms import profile_form


# def profile(request):
#     if request.method == "POST":
#         name= request.POST['name']
#         f_name= request.POST['father_name']
#         m_name= request.POST['mother_name']
#         email= request.POST['email']
#         r_no= request.POST['roll_no']
#         stream= request.POST['stream']
#         ad= request.POST['address']
#         state= request.POST['state']
#         c= request.POST['city']
#         p= request.POST['pin_code']
#         g= request.POST['gender']
#         m= request.POST['mobile_no']
#         i= request.POST['image']
#         d= request.POST['description']
#         myprofile(name=name, father_name=f_name, mother_name=m_name, email=email, roll_no=r_no, stream=stream, address=ad, state=state, city=c, pin_code=p, gender=g, mobile_no=m, image=i, description=d).save()
#         print(name,f_name,m_name,email,r_no,stream,ad,state,c,p,g,m,i,d)

 
#     return render(request,'profile.html')


def profileform(request):
    if request.method== "POST":
        a =profile_form(request.POST,request.FILES)
        print(a)
        
        if a.is_valid():
            
            name = a.cleaned_data['name']
            f_name = a.cleaned_data['father_name']
            m_name = a.cleaned_data['mother_name']
            email = a.cleaned_data['email']
            roll_no = a.cleaned_data['roll_no']
            stream = a.cleaned_data['stream']
            address =a.cleaned_data['address']
            state =a.cleaned_data['state']
            city =a.cleaned_data['city']
            pin_code= a.cleaned_data['pin_code']
            gender =a.cleaned_data['gender']
            mobile_no =a.cleaned_data['mobile_no']
            image=a.cleaned_data['image']
            description =a.cleaned_data['description']
            
            myprofile(name=name,father_name=f_name,mother_name=m_name,email=email,roll_no=roll_no,stream=stream,address = address,state = state,city = city,pin_code = pin_code,gender = gender,mobile_no = mobile_no,image = image,description = description).save()
            
            
            return HttpResponse('Data saved !!!')
        
    a =profile_form()
    context={
        'a':a
    }
    return render(request,'profile_form.html',context)        
    
    
def get_data(request):
    data= myprofile.objects.all()
    print(data)


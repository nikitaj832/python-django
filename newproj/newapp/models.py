from django.db import models

# Create your models here.
# class myresume(models.Model):
#     name = models.CharField(max_length=50)
#     date_of_birth = models.DateField()
#     post = models.CharField(max_length=50)
#     email = models.EmailField(max_length=150)
#     address = models.CharField(max_length=50)
#     mobile_no  = models.CharField(max_length=10)
#     image  = models.ImageField(upload_to='media',null=True)
#     linked_in = models.CharField(max_length=50)
#     skills=models.CharField(max_length=50)
#     description=models.CharField(max_length=400)
#     interest= models.CharField(max_length=100)
#     language= models.CharField(max_length=30)
#     education= models.CharField(max_length=500)
#     experience=models.CharField(max_length=400)
#     git=models.CharField(max_length=100)
    
class resume(models.Model):  
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media')
    ability=models.CharField(max_length=100)
    dob=models.DateField()
    mobile=models.CharField(max_length=14)
    email=models.EmailField(max_length=250)
    github_id=models.CharField(max_length=250)
    linkedin_id=models.CharField(max_length=250)
    address=models.CharField(max_length=50)
    years_degree=models.CharField(max_length=15)
    name_degree=models.CharField(max_length=30)
    clg_name=models.CharField(max_length=100)
    year12th=models.CharField(max_length=15)
    class_name12th=models.CharField(max_length=10)
    school_name12th=models.CharField(max_length=100)
    year10th=models.CharField(max_length=15)
    class_name10th=models.CharField(max_length=10)
    school_name10th=models.CharField(max_length=100)
    language_1=models.CharField(max_length=50)
    percentage_1=models.IntegerField()
    language_2=models.CharField(max_length=50)
    percentage_2=models.IntegerField()
    para_1=models.CharField(max_length=500)
    para_2=models.CharField(max_length=500)
    working_years_1=models.CharField(max_length=50)
    company_name_1=models.CharField(max_length=50)
    designation_1=models.CharField(max_length=50)
    about_1=models.CharField(max_length=250)
    working_years_2=models.CharField(max_length=50)
    company_name_2=models.CharField(max_length=50)
    designation_2=models.CharField(max_length=50)
    about_2=models.CharField(max_length=250)
    skill_1=models.CharField(max_length=50)
    percent_1=models.IntegerField()
    skill_2=models.CharField(max_length=50)
    percent_2=models.IntegerField()
    skill_3=models.CharField(max_length=50)
    percent_3=models.IntegerField()
    skill_4=models.CharField(max_length=50)
    percent_4=models.IntegerField()
    skill_5=models.CharField(max_length=50)
    percent_5=models.IntegerField()
    skill_6=models.CharField(max_length=50)
    percent_6=models.IntegerField()
    interest_1=models.CharField(max_length=50)
    interest_2=models.CharField(max_length=50)
    interest_3=models.CharField(max_length=50)
    interest_4=models.CharField(max_length=50)
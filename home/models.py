from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Personal(models.Model):
    name = models.CharField( max_length=50)
    mobile=models.CharField(max_length=13,default=None)
    email=models.EmailField(max_length=255)
    profile_picture = models.ImageField(upload_to ='',default='')
    sex=models.CharField(max_length=10)
    dob=models.DateField(max_length=8)
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    objective=models.CharField(max_length=500)
    user= models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.first_name

class Education(models.Model):
   
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)
    education = models.CharField(max_length=255)
    institute = models.CharField(max_length=255)
    percentage = models.PositiveIntegerField()
    passing_year = models.PositiveIntegerField()
    
    def __str__(self):
        return self.user.username

class Experience(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)   
    id=models.AutoField(primary_key=True)  
    company_name=models.CharField(max_length=255)
    location= models.CharField(max_length=255)
    joining_date=models.DateField()
    leaving_date=models.DateField()
    designation=models.CharField(max_length=50)
    workingOn=models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=255)
    project_desc = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

class SocialProfile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    social_profile = models.CharField(max_length=250)
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.user.username


class AdditionalInfo(models.Model):
    MARITAL_STATUS_CHOICES = (
        ('Single' , 'Single/Unmarried'),
        ('Married' , 'Married'),
        ('Divorced' , 'Divorced'),
        ('Seprated' , 'Seprated'),
        ('Other' , 'Other')
    )

    
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    skills = models.CharField(max_length=20)
    marital_Status = models.CharField(max_length=255 , choices=MARITAL_STATUS_CHOICES)
    website=models.URLField(max_length=255)
    language = models.CharField(max_length=150)


    def __str__(self):
        return self.user.username

class Certification(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    certification = models.CharField(max_length=250)
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.user.username
        
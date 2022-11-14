from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from home.models import *
# Create your views here.
def home(request):
    return render(request,'home/index.html')

def personal(request):
    if request.method == 'POST':
        user_id=request.user.id
        print("user...........................",user_id)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        picture = request.POST.get('picture')
        objective = request.POST.get('objective')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city= request.POST.get('city')

        messages.success(request, 'Your message has been sent!')
        details=Personal.objects.create(user_id=user_id, name=name,email=email,mobile=phone,dob=dob,profile_picture=picture,objective=objective,country=country,state=state,city=city)
        details.save()
        return render(request, 'home/index.html')
        
    # return HttpResponse("personal details")

def education(request):
    if request.method == 'POST':
        user_id=request.user.id
        institute = request.POST.get('institute')
        education = request.POST.get('education')
        percentage = request.POST.get('percentage')
        passing_year = request.POST.get('passing_year')

        messages.success(request, 'Your message has been sent!')
        details=Education.objects.create(user_id=user_id, institute=institute,education=education,percentage=percentage,passing_year=passing_year)
        details.save()
        return render(request, 'home/index.html')
    return HttpResponse('Education')
    # return render(request, 'home/index.html')

def experience(request):
    if request.method == 'POST':
        user_id=request.user.id
        company = request.POST.get('company')
        location = request.POST.get('location')
        joining_date = request.POST.get('joining_date')
        leaving_date = request.POST.get('leaving_date')
        designation = request.POST.get('designation')
        total_Experience = request.POST.get('total_Experience')

        messages.success(request, 'Your message has been sent!')
        details=Experience.objects.create(user_id=user_id, company_name=company,location=location,joining_date=joining_date,leaving_date=leaving_date,designation=designation,total_Experience=total_Experience)
        details.save()
        return render(request, 'home/index.html')
    return HttpResponse("experieance")

def project(request):
    if request.method == 'POST':
        user_id=request.user.id
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        summary = request.POST.get('summary')
        

        details=Project.objects.create(user_id=user_id, project_name=name,project_desc=desc,start_date=start_date,end_date=end_date,summary=summary)
        details.save()
        messages.success(request, 'Your message has been sent!')
        return render(request, 'home/index.html')
    return HttpResponse("Project")

def social(request):
    if request.method=='POST':
        user_id=request.user.id
        profile=request.POST.get('name')
        url=request.POST.get('url')

        details=SocialProfile.objects.create(user_id=user_id,social_profile=profile,url=url)
        details.save()
        messages.success(request, 'Your message has been sent!')
        return render(request,'home/index.html')
    return HttpResponse("Social Education")

def add_info(request):
    if request.method=='POST':
        user_id=request.user.id
        skills=request.POST.get('skills')
        marital_status=request.POST.get('marital_status')
        website=request.POST.get('website')
        language=request.POST.get('language')

        details=AdditionalInfo.objects.create(user_id=user_id,skills=skills,Marital_Status=marital_status,website=website,Language=language)
        details.save()
        messages.success(request, 'Your message has been sent!')
        return render(request,'home/index.html')
    return HttpResponse("Additional Info")

def certification(request):
    if request.method=='POST':
        user_id=request.user.id
        certification=request.POST.get('certification')
        url=request.POST.get('url')

        details=Certification(user_id=user_id,certification=certification,url=url)
        details.save()
        messages.success(request, 'Your message has been sent!')
        return render(request,'home/index.html')

    return HttpResponse("certification")

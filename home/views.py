from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

from home.models import *
from home.resume import generateResume

# Create your views here.
def home(request):
    return render(request,'home/index.html')

# @login_required
def personal(request):
    if request.method == 'POST':
        user_id=request.user.id
        # print("user...........................",user_id)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        sex = request.POST.get('sex')
        dob = request.POST.get('dob')
        picture = request.POST.get('picture')
        objective = request.POST.get('objective')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city= request.POST.get('city')

        messages.success(request, 'Your message has been sent!')
        details=Personal.objects.create(user_id=user_id, name=name,email=email,mobile=phone,sex=sex,dob=dob,profile_picture=picture,objective=objective,country=country,state=state,city=city)
        details.save()
        return redirect('home')
        
    # return HttpResponse("personal details")

def education(request):
    if request.method == 'POST':
        print("Education...")
        user_id=request.user.id
        institute = request.POST.get('institute')
        education = request.POST.get('education')
        percentage = request.POST.get('percentage')
        passing_year = request.POST.get('passing_year')

        messages.success(request, 'Your message has been sent!')
        details=Education.objects.create(user_id=user_id, institute=institute,education=education,percentage=percentage,passing_year=passing_year)
        details.save()
        return redirect('home')
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
        workingOn = request.POST.get('workingOn')

        messages.success(request, 'Your message has been sent!')
        details=Experience.objects.create(user_id=user_id, company_name=company,location=location,joining_date=joining_date,leaving_date=leaving_date,designation=designation,workingOn=workingOn)
        details.save()
        return redirect('home')
    return HttpResponse("experieance")

def project(request):
    if request.method == 'POST':
        user_id=request.user.id
        name = request.POST.get('name')
        desc = request.POST.get('desc')

        details=Project.objects.create(user_id=user_id, project_name=name,project_desc=desc)
        details.save()
        messages.success(request, 'Your message has been sent!')
        return redirect('home')
    return HttpResponse("Project")

def social(request):
    if request.method=='POST':
        user_id=request.user.id
        profile=request.POST.get('name')
        url=request.POST.get('url')

        details=SocialProfile.objects.create(user_id=user_id,social_profile=profile,url=url)
        details.save()
        messages.success(request, 'Your message has been sent!')
        return redirect('home')
    return HttpResponse("Social Education")

def add_info(request):
    if request.method=='POST':
        user_id=request.user.id
        skills=request.POST.get('skills')
        marital_status=request.POST.get('marital_status')
        website=request.POST.get('website')
        language=request.POST.get('language')

        details=AdditionalInfo.objects.create(user_id=user_id,skills=skills,marital_Status=marital_status,website=website,language=language)
        details.save()
        messages.success(request, 'Your message has been sent!')
        return redirect('home')
    return HttpResponse("Additional Info")

def certification(request):
    if request.method=='POST':
        user_id=request.user.id
        certification=request.POST.get('certification')
        url=request.POST.get('url')

        details=Certification(user_id=user_id,certification=certification,url=url)
        details.save()
        messages.success(request, 'Your message has been sent!')
        return redirect('home')

    return HttpResponse("certification")

def resume(request):
    id=request.user.id
    personal=Personal.objects.get(user_id=id)
    education=Education.objects.filter(user_id=id)
    experience=Experience.objects.filter(user_id=id)
    project=Project.objects.filter(user_id=id)
    social=SocialProfile.objects.filter(user_id=id)
    add_Info=AdditionalInfo.objects.get(user_id=id)
    # certify=Certification.objects.get(user_id=id)
    generateResume(personal=personal,education=education,experience=experience,projects=project,social=social,add_Info=add_Info)
    return HttpResponse(personal.name)
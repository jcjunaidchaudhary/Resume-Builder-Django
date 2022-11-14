from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    # return HttpResponse("junaid")
    return render(request,'authentication/index.html')

def signUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        password=request.POST.get('pass1')
        print('password',password,type(password))
        password2=request.POST.get('pass2')

        user=User.objects.create_user(username=username,email=email,password=password)
        user.first_name=firstname
        user.last_name=lastname
        user.save()

        messages.success(request,"Your account has been created")
        return redirect('signin')
    return render(request,'authentication/signup.html')


def signIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')

        print("username",username)

        
        user = authenticate(username=username, password = password)
        if user is not None:
            login(request, user)
            firstname = user.first_name
            return render (request, 'home/index.html', {'firstname': username})
        
        else:
            messages.error(request, "Bad request")
            return redirect('signin')
    return render(request, 'authentication/signin.html')
    
def signOut(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect('/accounts')


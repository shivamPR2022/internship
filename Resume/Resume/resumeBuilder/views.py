from email import message
from multiprocessing import context
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from resumeBuilder.models import user_profile
from resumeBuilder.models import Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def welcomeHome(request):
    return render(request,'E:/resume/Resume/template/welcomePage.html')
def contactUs(request):
    return render(request,'E:/resume/Resume/template/contactus.html')
def social(request):
    return render(request,'E:/resume/Resume/template/social.html')
def templte(request):
    return render(request,'E:/resume/Resume/template/templatesb.html')
def temp(request):
    
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']
        emailid=request.POST['emailid']        
        if password==password2:
            data=User.objects.create_user(first_name=firstname,last_name=lastname,password=password,email=emailid,username=username)
            data.save()
            return redirect('login')
        else:
            messages.info(request,"password check")
            return render(request,'E:/resume/Resume/template/Signup.html')

    else:
        return render(request,'E:/resume/Resume/template/Signup.html')

def login(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.info(request, "successfully log in")
            return redirect('home')
            
        else:
            messages.info(request,'check your username and password')
            return render(request,'E:/resume/Resume/template/login.html')

    else:  
        return render(request,"E:/resume/Resume/template/login.html")


def Logout(request):

            auth_logout(request)
            messages.info(request, "successfully log out")
            return redirect('home')

def ResumeTemplates(request):

    if request.method=='POST':
        
        Firstname=request.POST['name']
        sex:request.POST['sex']
        emailid=request.POST['emailid']  
        bod=request.POST['bod']   
        phone=request.POST['phone']

        userop=user_profile(firstname=Firstname,emailid=emailid,bod=bod,phone=phone)   
        userop.save()

        userop=user_profile.objects.get(firstname=Firstname)
        request.session['Firstname'] = Firstname
        return render(request,'E:/resume/Resume/template/categorydesign.html',{'userop':userop})
    else:
         return render(request,'E:/resume/Resume/template/tempform.html')

# def resume(request,id):
#     userop=user_profile.objects.get(firstname=id)
#     return render(request,'E:/resume/Resume/template/templatesb.html',{'userop':userop})

def format(request):
    Firstname = request.session['Firstname']
    context={
        "name":Firstname
    }
    userdata=user_profile.objects.get(firstname=Firstname)
    template_name="E:/resume\Resume/template/templatesb.html"
    return render(request,template_name,context)


        

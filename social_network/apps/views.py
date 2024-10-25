from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
# from .forms import CustomUserForm,OtpForm,CustomProfileForm
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User
from kavenegar import *
import logging
import json
from django.conf import settings
import http.client
import random


from django.contrib import messages


from django.contrib.auth.decorators import login_required

import pyotp

from datetime import datetime,timedelta

def custom_send_otp(request):
    totp=pyotp.TOTP(pyotp.random_base32(),interval=60)
    otp=totp.now()
    request.session['otp']=otp
    request.session['otp_secret_key']=totp.secret
    valid_date=datetime.now()+timedelta(minutes=1)
    request.session['otp_valid_date']=str(valid_date)
    print(f"one time password {otp}")
    return otp



def send_otp(request,mobile): #,otp=None):
    otp=random.randint(1000,999999)
    api=KavenegarAPI('35776656675A494638504B526A6D787A50626C39756B4A4D534A484349614E576F4B756C4D2F4A534276733D')
    params={
        'sender':'',  #'1000689696',
        'receptor':'09229479057',
        'message':f"{otp}",
    }
    response = api.sms_send( params)
    print(response)
    print(mobile)
    return otp


# def register(request):
#     if request.method=="POST":
#         form=CustomUserForm(request.POST)
#         if form.is_valid():
#             request.session['mobile']=form.cleaned_data['mobile']
#             print(request.session['mobile'])
#             custom_send_otp(request)
#             request.session['email']=form.cleaned_data['email']
#             print(request.session['email'])
#             request.session['username']=form.cleaned_data['username']
#             print(request.session['username'])
#             request.session['password']=form.cleaned_data['password']
#             print(request.session['password'])
#             user=User.objects.create_superuser(username=request.session['username'],email=request.session['email'],password=request.session['password'])
#             user.save()
#             return redirect("apps:otp_view")
#         else:
#             return HttpResponse("invalidinput")
#     else:
#         form=CustomUserForm()
#         return render(request,"apps/register/register.html",{"form":form})

# def login_view(request):
#     if request.method=="POST":
#         form=AuthenticationForm(request, data=request.POST)
#         if  form.is_valid():
#             user_name=form.cleaned_data['username']
#             password=form.cleaned_data['password']
#             user=authenticate(username=user_name,password=password)
#             if user  is not None :
#                 user.save()
#                 login(request,user)
#                 messages.info(request, f"You are now logged in as {user_name}.")
#                 return redirect('apps:main_view')
#             else:
#                 return HttpResponse("Invalid username or password.")
#         else:
#            return HttpResponse("Invalid username or password.")
#     form=AuthenticationForm()
#     return render(request,'apps/login/login.html',{'form':form}) 

# def otp_view(request):
#     form=OtpForm()
#     otp=request.session['otp']
#     if request.method=="POST":
#         form=OtpForm(request.POST)
#         if form.is_valid():
#             otp_form=form.cleaned_data['otp']
#             form.clean()
#             if otp==otp_form:
#                 username=request.session['username']
#                 print(username)
#                 password=request.session['password']
#                 print(password)
#                 if username and password:
#                     user = authenticate(request, username=username, password=password)
#                     login(request,user)
#                     print(1)
#                 else:
#                     return HttpResponse("Username and password are required")
#                 # user = authenticate(request, username=username,password=password)
#                 # user = authenticate(request, username=request.POST["username"],password=request.POST["password"])
#                 #     # print(username)login(request, user)
#                 #     print("logined")
#                 # if user is not None:
#                 return redirect("apps:main_view")
#                 # else:
#                 #     pass    
#             else:
#                 return HttpResponse("invalid otp")
#         else:
#             return HttpResponse("invalid input")
#     return render(request,"apps/otp/otp.html",{'form':form})



# def main_view(request):
#     return render(request,"apps/main/main.html",{})


# @login_required
# def logout_view(request):
#     logout(request)
#     redirect("apps:main_view")
    
    
# @login_required
# def create_profile_view(request):
#     form=CustomProfileForm()
#     if request.method=="POST":
#         form=CustomProfileForm(request.POST)
#         if form.is_valid():
#             form1=form.save(commit=False)
#             users=User.objects.get(username=request.user.username)
#             mobile=request.session['mobile']
#             form1.user=users
#             form1.mobile=mobile
#             form1.save()
#             form1.clean()
#             return redirect("apps:main_view")
#         else:
#             messages.error(request,"invalid input")
#             return render(request,"apps/profile/profile.html",{'form':form})
#     else:
#         return render(request,"apps/profile/profile.html",{'form':form})
       


# @login_required
# def chang_password(request):
#     user=User.objects.get(username=request.user.username)
#     return 3https://github.com/ahmad-donesee/social_network
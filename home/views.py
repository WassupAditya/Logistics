

# Create your views here.
from django import contrib
from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime 
from firebase import firebase
from requests import post,get

from firebase.firebase import FirebaseApplication, FirebaseAuthentication



from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import SESSION_KEY, authenticate
from django.contrib.auth import logout,login

import pyrebase 
from pyrebase.pyrebase import  Database

 
config = {    
  "apiKey": "AIzaSyB01qJKJ1uSihQAfIYybkQ6LSG6MveiCEk",
  "authDomain": "project1-aa36f.firebaseapp.com",
  "databaseURL": "https://project1-aa36f-default-rtdb.firebaseio.com",
  "projectId": "project1-aa36f",
  "storageBucket": "project1-aa36f.appspot.com",
  "messagingSenderId": "70593293088",
  "appId": "1:70593293088:web:dc3bf981ac7015a359c545",
  "measurementId": "G-2S7DMQS079"
}
 
firebase = pyrebase.initialize_app(config) 

authe = firebase.auth() 

database = firebase.database()


def index(request):
    #context = {"variable1": "Harry is great", "variable2": "Rohan is great"}
    #return HttpResponse("This is homepage")
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html') 

def about(request):
    return render(request, 'about.html')


    #return HttpResponse("This is aboutpage")
def services(request):
    return render(request, 'services.html')    
 
def prelogin(request):
    return render(request,'prelogin.html')  
      
def adminlogin(request):
    return render(request,'login1.html')    
def login2(request):
    return render(request,'login2.html')    
def login3(request):
    return render(request,'login3.html')    
def login4(request):
    return render(request,'login4.html')

def admin1 (request) :
    return render(request , "admin1.html")    
def admin2 (request) :
    return render(request , "admin2.html")    
def admin3 (request) :
    return render(request , "admin3.html")    
def admin4 (request) :
    return render(request , "admin4.html")    

def postadmin1 (request) :
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw1 = request.POST.get('pass')
    address = request.POST.get('add')
    country = request.POST.get('count')
    state = request.POST.get('state')
    city = request.POST.get('city')
    pincode = request.POST.get('pin')
    phone = request.POST.get('phone')
    
     
    user=authe.create_user_with_email_and_password(email,passw1)
    session_id=user['idToken']
    request.session['uid']=str(session_id)
        #push data 
    data={
        "name" :name ,
        "email" : email ,
        "address" : address ,
            "country" : country ,
            "state":state,
            "city":city,
            "pincode":pincode,
            "phone":phone
            
        }
    database.child("Data").child("Signup").child("user1").push(data)
    print("User created")
    messages.success(request, 'Your have successfully registered!')
    return render(request,"adminhome.html")

def postadmin2 (request) :
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw1 = request.POST.get('pass')
    address = request.POST.get('add')
    country = request.POST.get('count')
    state = request.POST.get('state')
    city = request.POST.get('city')
    pincode = request.POST.get('pin')
    phone = request.POST.get('phone')
    
     
    user=authe.create_user_with_email_and_password(email,passw1)
    session_id=user['idToken']
    request.session['uid']=str(session_id)
        #push data 
    data={
        "name" :name ,
        "email" : email ,
        "address" : address ,
            "country" : country ,
            "state":state,
            "city":city,
            "pincode":pincode,
            "phone":phone
            
        }
    database.child("Data").child("Signup").child("user2").push(data)
    print("User created")
    messages.success(request, 'Your have successfully registered!')
    return render(request,"adminhome.html")
def postadmin3 (request) :
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw1 = request.POST.get('pass')
    address = request.POST.get('add')
    country = request.POST.get('count')
    state = request.POST.get('state')
    city = request.POST.get('city')
    pincode = request.POST.get('pin')
    phone = request.POST.get('phone')
    
     
    user=authe.create_user_with_email_and_password(email,passw1)
    session_id=user['idToken']
    request.session['uid']=str(session_id)
        #push data 
    data={
        "name" :name ,
        "email" : email ,
        "address" : address ,
            "country" : country ,
            "state":state,
            "city":city,
            "pincode":pincode,
            "phone":phone
            
        }
    database.child("Data").child("Signup").child("user3").push(data)
    print("User created")
    messages.success(request, 'Your have successfully registered!')
    return render(request,"adminhome.html")

def postadmin4 (request) :
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw1 = request.POST.get('pass')
    address = request.POST.get('add')
    country = request.POST.get('count')
    state = request.POST.get('state')
    city = request.POST.get('city')
    pincode = request.POST.get('pin')
    phone = request.POST.get('phone')
    
     
    user=authe.create_user_with_email_and_password(email,passw1)
    session_id=user['idToken']
    request.session['uid']=str(session_id)
        #push data 
    data={
        "name" :name ,
        "email" : email ,
        "address" : address ,
            "country" : country ,
            "state":state,
            "city":city,
            "pincode":pincode,
            "phone":phone
            
        }
    database.child("Data").child("Signup").child("user4").push(data)
    print("User created")
    messages.success(request, 'Your have successfully registered!')
    return render(request,"adminhome.html")    
    
def login (request) :
    email = request.POST.get('username')
    passwd =  request.POST.get('password')
     
    try:
         
        
        # if there is no error then signin the user with given email and password
        user=authe.sign_in_with_email_and_password(email,passwd)
        session_id=user['idToken']
        request.session['uid']=str(session_id)
        return render(request , 'adminpanel.html')
    except:
        message="Invalid Credentials!!Please ChecK your Data"
        return render(request,"login1.html",{"message":message}) 



        
def login2(request) :
   
    email = request.POST.get('username')
    passwd =  request.POST.get('password')

    firebase=FirebaseApplication("https://project1-aa36f-default-rtdb.firebaseio.com/", None)
    result=firebase.get('/Data/Signup/user2', None)
    flag=0
    for userid,user in result.items():
            if email==user['email'] :    
                flag=1
                
                # if there is no error then signin the user with given email and password
                user=authe.sign_in_with_email_and_password(email,passwd)
                session_id=user['idToken']
                request.session['uid']=str(session_id)
                        
                return render(request , 'lh1.html')
                break;
            else:
                messages.warning(request, 'Invalid Credentials!!Please Check your Data')    
    if flag==0:
                
        message="Invalid Credentials!!Please ChecK your Data"
        return render(request,"login2.html",{"message":message})


def login3(request) :
    email = request.POST.get('username')
    passwd =  request.POST.get('password')
    
    firebase=FirebaseApplication("https://project1-aa36f-default-rtdb.firebaseio.com/", None)
    result=firebase.get('/Data/Signup/user3', None)
    flag=0
    for userid,user in result.items():
            if email==user['email'] :    
                flag=1
                
                # if there is no error then signin the user with given email and password
                user=authe.sign_in_with_email_and_password(email,passwd)
                session_id=user['idToken']
                request.session['uid']=str(session_id)
                        
                return render(request , 'lh2.html')
                break;
            else:
                messages.warning(request, 'Invalid Credentials!!Please Check your Data')    
    if flag==0:
                
        message="Invalid Credentials!!Please ChecK your Data"
        return render(request,"login3.html",{"message":message}) 
         
def login4(request) :
    email = request.POST.get('username')
    passwd =  request.POST.get('password')
    
    firebase=FirebaseApplication("https://project1-aa36f-default-rtdb.firebaseio.com/", None)
    result=firebase.get('/Data/Signup/user4', None)
    flag=0
    for userid,user in result.items():
            if email==user['email'] :    
                flag=1
                
                # if there is no error then signin the user with given email and password
                user=authe.sign_in_with_email_and_password(email,passwd)
                session_id=user['idToken']
                request.session['uid']=str(session_id)
                       
                return render(request , 'lh3.html')
                
            else:
                messages.warning(request, 'Invalid Credentials!!Please Check your Data')
                message="Invalid Credentials!!Please ChecK your Data"
                return render(request,"login4.html",{"message":message})
    
    if flag==0:
                
        message="Invalid Credentials!!Please ChecK your Data"
        return render(request,"login4.html",{"message":message})

def adminpanel(request):
     pass
        
def lh1(request):
     pass
        
def lh2(request):
     pass
        
def lh3(request):
     messages.success(request, 'You have successfully logged in')  
     pass
        

 

    

           
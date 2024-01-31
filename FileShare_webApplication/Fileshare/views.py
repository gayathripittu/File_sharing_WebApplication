from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
import psycopg2 as db
import base64
import binascii
import functools
import hashlib
import importlib
from django.contrib.auth.hashers import make_password
import django.utils.encoding 
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from Fileshare.models import userdata,filedata
from Fileshare.forms import loginform,signupform,upload_f
from Fileshare.functions import handle_uploaded_file




def index(request):
    return render(request,'home.html')

def signup(request):
    mydata=userdata.objects.all()    
    myform=signupform()
    if mydata!='':
        context={'form':myform,'mydata':mydata}
        return render(request,'signup.html',context)
    else:
        context={'form':myform}
        return render(request,"signup.html",context)
def login(request):
    global pwds,email
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        password=hashlib.sha256(password.encode()).hexdigest()
        #user = userdata.objects.raw('SELECT * FROM fileshare_userdata')[0]
        user=userdata.objects.all().filter(email=email,password=password)
        exists=userdata.objects.filter(email=email).exists()
        print(exists)
        
        if len(user)==1:
            messages.success(request,"account created successfully.")
            return render(request, 'result.html')
        elif(exists=='False'):
            messages.error(request,'user %s does not exists...!!!'% email)
            myform=loginform()
            return render(request,'login.html',{'form':myform})

        else:
            messages.error(request,'incorrect email or password')
            myform=loginform()
            return render(request,'login.html',{'form':myform})
        
    else:
            myform=loginform()
            return render(request,'login.html',{'form':myform})

def upload(request):
    mydata=filedata.objects.all()    
    myform=upload_f()
    if mydata!='':
        context={'form':myform,'mydata':mydata}
        return render(request,'upload.html',context)
    else:
        context={'form':myform}
        return render(request,"upload.html",context)

def file_upload(request):
        if request.method=="POST":
            myform=upload_f(request.POST,request.FILES)
            if myform.is_valid():
                r_email=request.POST.get('r_email')
                key=request.POST.get('key')
                file=request.FILES.get('file')
                exists=filedata.objects.filter(file=file).exists()

            if exists:
                messages.error(request,'The file %s is already exists...!!!'% file)
            else:
                key=hashlib.sha256(key.encode()).hexdigest()
                filedata.objects.create(r_email=r_email,file=file,key=key).save()
                messages.success(request,"File uploaded successfully.")
        return redirect("upload")
    #return render(request,'upload.html')

def fileview(request):
    all_data=filedata.objects.all()
    data=filedata.objects.all().filter(r_email=email)
    print(data.values())

    context={
        'data':data
    }
    return render(request,"fileview.html",context)
    #return render(request,'fileview.html')

def result(request):
    return render(request,'result.html')
def logout(request):
    return render(request,'home.html')

def uploaddetails(request):
    if request.method=="POST":
        myform=signupform(request.POST)        
        if myform.is_valid():
            name = request.POST.get('name') 
            email = request.POST.get('email')
            pwd = request.POST.get('password') 
            c_password = request.POST.get('c_password') 
            
            password=hashlib.sha256(pwd.encode()).hexdigest()

            exists=userdata.objects.filter(email=email).exists()
            res=password_checker(pwd)
            ret=1

            if(len(pwd)<8):
                ret=0
                messages.error(request,'password should be minimum 8 characters')
            elif(ret):
                res=password_checker(pwd)
                print(res,pwd,c_password)
                if(res==1):
                    ret=1
                elif(res==2):
                    ret=0
                    messages.error(request,'your password is weak, please create a strong password')
                else:
                    ret=0
                    messages.error(request,'Your Password must contain atleast a special character, number, uppercase and lowercase letters')

            elif(pwd!=c_password and ret==1):
                messages.error(request,'confirm password should be the same as password')
            elif exists:
                messages.error(request,'The email %s is already exists..please login.!!!'% email)

            else:
                pass
            if(ret==1):
                print("account created")
                userdata.objects.create(name=name,email=email,password=password).save()
                messages.success(request,"account created successfully.")
        return redirect("signup")

import re
import os

    
def password_checker(user_password): 
    a='1234567890'                  
    b='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s_l='abcdefghijklmnopqrstuvwxyz'
    c='!@#$^&()_.-'
    word_list=['123456', '123456789', 'picture1', 'password', '12345678', '111111', '123123', '12345', '1234567890', 'senha', '1234567', 'qwerty', 'abc123', 'Million2', '00000000', '1234', 'iloveyou', 'aaron431', 'password1', 'qqww1122', '123', 'omgpop', '123321', '654321', 'qwertyuiop', 'qwer123456', '123456a', 'a123456', '666666', 'asdfghjkl', 'ashley', '987654321', 'unknown', 'zxcvbnm', '112233', 'chatbooks', '20100728', '123123123', 'princess', 'jacket025', 'evite', '123abc', '123qwe', 'sunshine', '121212', 'dragon', '1q2w3e4r', '5201314', '159753', '123456789', 'pokemon', 'qwerty123', 'Bangbang123', 'jobandtalent', 'monkey', '1qaz2wsx', 'abcd1234', 'default', 'aaaaaa', 'soccer', '123654', 'ohmnamah23', '12345678910', 'zing', 'shadow', '102030', '11111111', 'asdfgh', '147258369', 'qazwsx', 'qwe123', 'michael', 'football', 'baseball', '1q2w3e4r5t', 'party', 'daniel', 'asdasd', '222222', 'myspace1', 'asd123', '555555', 'a123456789', '888888', '7777777', 'fuckyou', '1234qwer', 'superman', '147258', '999999', '159357', 'love123', 'tigger', 'purple', 'samantha', 'charlie', 'babygirl', '88888888', 'jordan23', '789456123', 'jordan', 'anhyeuem', 'killer', 'basketball', 'michelle', '1q2w3e', 'lol123', 'qwerty1', '789456', '6655321', 'nicole', 'naruto', 'master', 'chocolate', 'maggie', 'computer', 'hannah', 'jessica', '123456789a', 'password123', 'hunter', '686584', 'iloveyou1', '987654321', 'justin', 'cookie', 'hello', 'blink182', 'andrew', '25251325', 'love', '987654', 'bailey', 'princess1', '123456', '101010', '12341234', 'a801016', '1111', '1111111', 'anthony', 'yugioh', 'fuckyou1', 'amanda', 'asdf1234', 'trustno1', 'butterfly', 'x4ivygA51F', 'iloveu', 'batman', 'starwars', 'summer', 'michael1', 'lovely', 'jakcgt333', 'buster', 'jennifer', 'babygirl1', 'family', '456789', 'azerty', 'andrea', 'q1w2e3r4', 'qwer1234', 'hello123', '10203', 'matthew', 'pepper', '12345a', 'letmein', 'joshua', '131313', '123456b', 'madison', 'Sample123', '777777', 'football1', 'jesus1', 'taylor', 'b123456', 'whatever', 'welcome', 'ginger', 'flower', '333333', '1111111111', 'robert', 'samsung', 'a12345', 'loveme', 'gabriel', 'alexander', 'cheese', 'passw0rd', '142536', 'peanut', '11223344', 'thomas', 'angel1']
    # word_list contains the most used passwords
    special,freq,number,alpha,small=0,0,0,0,0
    
    for element in word_list:              
        if(re.search(element,user_password.lower())):  # checking the password is matching with pattern of most used passwords
            freq=freq+1
            break
        

    if(freq==0):   # checking the length of password, it should be atleast 8 characters
        for i in user_password:
            if i in b:
                alpha=alpha+1               # counting the no.of uppercase letters in password
            elif i in a:
                number=number+1             # counting the no.of numbers in password         
            elif i in c:
                special=special+1           # counting the no.of special characters in password
            elif i in s_l:
                small=small+1               # counting the no.of lowercase letters in password
        if alpha>0 and special>0 and number>0 and small>0:                                     # condition to check password is containing atleast 1 uppercase, 1 lowercase, 1 special character and 1 number
            return 1                             # condition is true print strong
        else: 
            return 3               
    else:
        return 2
    








            


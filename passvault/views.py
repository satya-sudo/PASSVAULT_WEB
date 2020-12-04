from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse


from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .models import User,SavedPassword
from django.db import IntegrityError

from .util import passHash,unhashpass

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('userMenu'))

    return render(request,"passvault/index.html")

def TC(request):
    return render(request,"passvault/TC.html")
    

def login_view(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('userMenu'))

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:

            login(request,user)    
            return render(request,'passvault/signinmenu.html')
        else:
            return render(request,'passvault/signin.html',{'message':"Invalid username and/or password."})
                
    return render(request,'passvault/signin.html')

def register(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('userMenu'))

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']

        password = request.POST['password']
        confirm = request.POST['confirm']

        if password != confirm:
            return render(request,'passvault/signup.html',{'message':'Passwords Must Match'})
        try:
            user = User.objects.create_user(username,email,password)
            user.save()  
            login(request,user)
            return HttpResponseRedirect(reverse("userMenu"))
            
        except IntegrityError:
            return render(request,'passvault/signup.html',{'message':'Sorry Username Already Taken!'})
            
    return render(request,'passvault/signup.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index")) 

@login_required(login_url='/login')
def userMenu(request):
    return render(request,'passvault/signinmenu.html')
    
@login_required(login_url='/login')
def AddCred(request):
    if request.method == 'POST':
        SiteName = request.POST['Sitename']
        SiteUserName =  request.POST['siteusername']
        password = passHash(request.user.username,request.POST['password'])
        

        newCred = SavedPassword(user=request.user,SiteName=SiteName,SiteUserName=SiteUserName,PasswordForSite=password)
        newCred.save()
        return HttpResponseRedirect(reverse("userMenu"))

    return render(request,'passvault/newCred.html')

@login_required(login_url='/login')
def search(request):
    if request.method == 'POST':
        query = request.POST['Searchquery']
        try:
            user = request.user
            passwords = user.SitePasswords.all().filter(SiteName__icontains=query)
            for i  in passwords:
                i.PasswordForSite = unhashpass(request.user.username,i.PasswordForSite)
            return render(request,'passvault/found.html',{'resultTitle':f'Found results for {query}','results':passwords})
        except:
            pass

    return render(request,'passvault/search.html')    
        
@login_required(login_url='/login')       
def getallpassword(request):
    try:
        user = request.user
        passwords = user.SitePasswords.all()
        for i  in passwords:
            i.PasswordForSite = unhashpass(request.user.username,i.PasswordForSite)
    except:
        return render(request,'passvault/found.html')
        
    return render(request,'passvault/found.html',{'results':passwords})
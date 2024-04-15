from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def home(request):
   return render(request,"authentication/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        name = request.POST.get('name')
        sem = request.POST.get('sem')
        classd = request.POST.get('classd')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm= request.POST.get('confirm')
        security = request.POST.get('security')
        
        myuser = User.objects.create_user(username,email,password)
        myuser.name=name
        myuser.sem=sem
        myuser.classd=classd
        myuser.security=security
        myuser.save()
        messages.success(request,"Your account successfully created")
        return redirect('signin')
    return render(request,"authentication/signup.html")

def signin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        securityanswer=request.POST.get('securityanswer')

        user = authenticate(username=username,password=password,securityanswer=securityanswer)
        if user is not None:
            login(request,user)
            name=user.username
            return render(request,"authentication/index.html", {"name":name})
        else:
            messages.error(request,"Bad Credentials")
            return redirect('home')

    return render(request,"authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "logged out successfully!")
    return redirect("home")

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User,auth

# Create your views here.
def cv(request):
    return render(request, 'cv.html')


def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(cv)
        else:
            messages.success(request,'Login failed')
            return redirect(login)

    return render(request, 'login.html')

def registration(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request,"User arleady exist")
                return redirect('registration')
            elif User.objects.filter(email = email).exists():
                messages.error(request,"Email arleady used")
                return redirect('registration')
            else:
                user=User.objects.create_user(username= username,password= password1, email= email)
                user.set_password(password1)
                user.save()
                messages.success(request,"Profile successfully created")
                return redirect('login')
    return render(request, 'registration.html')

def createProf(request):
    return render(request, 'index.html')

def forgot(request):
    return render(request, 'forgot.html')
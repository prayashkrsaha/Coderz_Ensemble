from django.shortcuts import render , HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.
def lgin(request):
    if request.method == "POST":
        username=request.POST['email']
        password=request.POST['password']
        check_if_user_exists = User.objects.filter(username=username).exists()
        if check_if_user_exists:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/dashboard")
            else:
                messages.warning(request, 'Oops!..Wrong Password')
                return redirect("/")
        else:
            messages.warning(request, 'Oops....seems You dont have an account....Create one now')
            return render(request,"signup.html")
    return render(request,"lgin.html")

def signup(request):
    if request.method == "POST":
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        check_if_user_exists = User.objects.filter(username=username).exists()
        
        if username!="" and password!="":
            if check_if_user_exists:
                messages.warning(request, 'Oops....the Username already exists try a different one')
                return redirect("/signup")
            else:
                user=User.objects.create_user(username,email,password)
                user.save()
                messages.success(request, 'WELCOME....You Signed sucessfully')
                return redirect("/")
        else:
            messages.warning(request, 'Oops!..Required Field not filled')
            return redirect("/signup")
    return render(request,"signup.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def dashboard(request):
    return render(request,"dashboard.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def learn(request):
    return render(request,"learn.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def cp(request):
    return render(request,"cp.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/')
def editor(request):
    return render(request,"editor.html")

def lgout(request):
    logout(request)
    return redirect("/")
    
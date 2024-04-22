from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_user(request):
    if request.user.is_authenticated:
        return redirect("home:home")
        

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home:home")
        else:
            pass

    return render(request, "account/login.html", context={})




def logout_user(request):
    logout(request)
    return redirect("home:home")



def register(request):
    if request.user.is_authenticated:
        return redirect("home:home")
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        login(request, User.objects.create_user(username=username, email=email, password=password1 and password2))
        return redirect("home:home")
    
    return render(request, "account/register.html")
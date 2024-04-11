from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout


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


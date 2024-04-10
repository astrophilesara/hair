from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            pass
  
    return render(request, "account/login.html", context={})

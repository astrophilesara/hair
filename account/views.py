from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm,RegisterForm
from django.views.generic import FormView


def login_user(request):
    if request.user.is_authenticated:
        return redirect("home:home")
        

    if request.method == "POST":
        # username = request.POST["username"]
        # password = request.POST["password"]
        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     return redirect("home:home")

        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            user = User.objects.get(username=username)
            login(request, user)
            return redirect("home:home")

    else:
        form = LoginForm()
    return render(request, "account/login.html", context={"form" : form})






def logout_user(request):
    logout(request)
    return redirect("home:home")






# def register(request):
#     context = {"errors" : []}
#     if request.user.is_authenticated:
#         return redirect("account:login")
   
#     if request.method == "POST":
#         # username = request.POST["username"]
#         # email = request.POST["email"]
#         # password1 = request.POST["password1"]
#         # password2 = request.POST["password2"]
#         # login(request, User.objects.create_user(username=username, email=email, password=password1 and password2))
#         # return redirect("home:home")
    
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             email = form.cleaned_data.get("email")
#             password1 = form.cleaned_data.get("password1")
#             password2 = form.cleaned_data.get("password2")
#             form.save()
#             if password1 != password2:
#                 context["errors"].append("Passwords are not same")
#                 return render (request, "account/register.html", context)
            
#             user = User.objects.create_user(username=username, email=email, password=password1 and password2)
#             login(request, user)
#             return redirect("home:home")
#     else: 
#         form = RegisterForm


#     return render(request, "account/register.html")




class RegisterView(FormView):
    template_name = "account/register.html"
    form_class = RegisterForm
    success_url = "home:home"
    
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    

    def form_invalid(self, form): 
        return self.render_to_response(self.get_context_data(form=form))
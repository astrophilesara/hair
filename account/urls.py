from django.urls import path 
from . import views
from account.views import RegisterView


app_name = "account"

urlpatterns = [
    path("login/", views.login_user, name = "login"),
    path("logout/", views.logout_user, name = "logout"),
    path("register/", RegisterView.as_view(), name = "register"),
]
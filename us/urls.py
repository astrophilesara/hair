from django.urls import path 
from . import views


app_name = "us"

urlpatterns = [
    path("about/", views.us, name = "about"),
]
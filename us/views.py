from django.shortcuts import render

# Create your views here.


def about(request):
    return render(request, "us/about.html", context={})



def contact(request):
    return render(request, "us/contact.html", context={})
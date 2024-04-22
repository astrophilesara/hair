from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.
# def home(request):
#     return render(request, "home/index.html", context={})


class HomeView(TemplateView):
    template_name = "home/index.html"



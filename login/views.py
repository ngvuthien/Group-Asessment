from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"login/login.html")
def register(request):
    return render(request,"login/register.html")
  
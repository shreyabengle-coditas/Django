from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def admin_login(request):
    return HttpResponse("Logged in successfully")


def admin_control(request):
    return HttpResponse("<h1>I have control</h1>")

def admin_var1(request):
    a=10+10
    return HttpResponse(a)

def admin_math1(request):
    a=10*10
    return HttpResponse(a)
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    with open('C:/Users/shreya.bengle_codita/Documents/Django/School_project/homepage.PNG', 'rb') as f:
        image_data = f.read()   
    return HttpResponse(image_data, content_type='image/png')
    
def learn_django(request):
    return HttpResponse("Learn Django")


def learn_python(request):
    return HttpResponse("<h1> Python</h1>")

def learn_var(request):
    a=10+10
    return HttpResponse(a)

def learn_math(request):
    a=10*10
    return HttpResponse(a)
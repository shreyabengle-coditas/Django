from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.
def view_one(request):
    return render(request,'template_one.html')


def view_two(request):
    return render(request,'template_two.html')


def hello(request):
    return redirect("https://www.google.co.in/")
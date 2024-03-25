from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fee_paid(request):
    return HttpResponse("ALL paid")


def fee_due(request):
    return HttpResponse("<h1>Fees due by these members:</h1>")

def fee_remaning(request):
    a=10+10
    return HttpResponse(a)

def fee_amt(request):
    a=10*10
    return HttpResponse(a)

from django.shortcuts import render
from django.http import HttpResponse
 
# Create your views here.
def view_appointment(request):
    return HttpResponse("The appointment schedule is as follow:<br> 1) 10-11 <br> 2)11-12")

def access_records(request):
    patient="Shreya"
    return HttpResponse(f"The medical records of {patient} is as follows:")


def prescription(request):
    return HttpResponse("The prescription is as follows:")


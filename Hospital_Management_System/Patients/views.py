from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("<h1>HOMEPAGE</h1>")
def schedule_appointment(request):
    return HttpResponse("<h1>Appointment Scheduled</h1>")

def medical_history(request):
    return HttpResponse("<h1>Medical history</h1><br><h2>Previous Records</h2>")

def notifications(request):
    with open('C:/Users/shreya.bengle_codita/Documents/Django/Hospital_Management_System/Image.PNG', 'rb') as f:
        image_data1 = f.read()   
    return HttpResponse(image_data1, content_type='Image/PNG')
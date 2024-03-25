from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def management(request):
    return HttpResponse("Number of rooms:10 <br> Number of resources:20 <br> Number of equipments:14")


def reports(request):
    with open('C:/Users/shreya.bengle_codita/Documents/Django/Hospital_Management_System/Report.PNG', 'rb') as f:
        image_data = f.read()   
    return HttpResponse(image_data, content_type='Image/PNG')
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
# Create your views here.
@csrf_exempt
def display(request):
    if request.method=='POST':
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        dob = request.POST.get('date_of_birth')

        insert_data = models.Student(f_name= f_name,l_name=l_name, dob = dob)
        insert_data.save()

        data = models.Student.objects.all()
        # print(data)
        
        # return HttpResponse(f_name)
    # else: 
        return render(request,'student_data.html',{'data':data})
    return render(request,'student_data.html')

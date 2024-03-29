from django.shortcuts import render, redirect
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
        image= request.FILES.get('photo')
        resume= request.FILES.get('resume')
        insert_data = models.Student(f_name= f_name,l_name=l_name, dob = dob, image=image, resume=resume)
        insert_data.save()

        data = models.Student.objects.all()
        # print(data)
        
        # return HttpResponse(f_name)
    # else: 
        return render(request,'NextPage.html',{'data':data})
        
    return render(request,'student_data.html')
@csrf_exempt
def new_page(request):
    if request.method=='POST':
        return redirect(display)
    return render(request,'NextPage.html')

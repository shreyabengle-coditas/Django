from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def addition(request):
    if request.method=='POST':
        num1= request.POST.get('number1',0)
        num2= request.POST.get('number2',0)
        result= int(num1)+int(num2)
        print(f"Result:{result}")
        return HttpResponse(result)
    else:
        return render(request,'add.html')

   
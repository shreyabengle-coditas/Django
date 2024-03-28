from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def view_books(request):
    # if request.method == 'POST':
    #     return redirect(add_books)
    return render(request, "view_books.html")

@csrf_exempt
def add_books(request):
    if request.method == 'POST':
        return redirect(view_books)
    return render(request,'add_books.html')
    

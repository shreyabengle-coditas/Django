from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view_books(request):
    return render(request, "view_books.html")
    

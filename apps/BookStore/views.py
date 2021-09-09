from django.shortcuts import render
from .admin import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def books(request):
    allproduct = libros.objects.all()
    return render(request, 'books.html', {'LibrosStock':allproduct})

def contact(request):
    return render(request, 'contact.html')

def library(request):
    return render(request, 'library.html')
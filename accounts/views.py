from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello World")  

def products(request):
    return HttpResponse("Products") 

def customer(request):
    return HttpResponse("Customer") 

# Create your views here.

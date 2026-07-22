
from django.http import HttpResponse
from django.shortcuts import render

def index(req):
    context = { 
        "message" : 'Welcome to Ecommerce Website'
    }
    return render(req , 'index.html' , context)
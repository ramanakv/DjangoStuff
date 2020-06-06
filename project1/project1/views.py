from django.http import HttpResponse
from django.shortcuts import render


def sayHello(request):
    return  HttpResponse("<h1>Hello World</h1>")

def welcome(request):
    data = {
     'name':'Ramana',
     "training":'Django'
    }

    return render(request,"welcome.html",{"content":data})

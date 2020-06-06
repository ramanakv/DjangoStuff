from django.shortcuts import render
from .models import Person
from django.http import HttpResponse
# Create your views here.

def getAll1(request):
    persons = Person.objects.all()
    names = list()

    for p in persons:
        names.append(p.name)
    response_html = '<br>'.join(names)
    return HttpResponse(response_html)

def getAll2(request):
    persons = Person.objects.all()
    print(persons)
    return render(request,"persons.html",{'persons':persons})
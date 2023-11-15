from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def virat(request):
    return HttpResponse('<h1>50th Century By Virat...Record Breaked</h1>')

def shami(request):
    return render(request,'shami.html')
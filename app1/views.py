from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def rohit(request):
    return HttpResponse('<h1>Best Captain Now a Days Cricket</h1>')


def bumrah(request):
    return render(request,'bumrah.html')
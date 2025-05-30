from django.shortcuts import render
from django.http import HttpResponse

def showinfinity(request):
    return HttpResponse("Hello world!")
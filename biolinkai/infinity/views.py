from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def showinfinity(request):

    return render(request, 'index.html')
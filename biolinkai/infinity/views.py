from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Infinity

def showinfinity(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        phoneno=request.POST.get('phoneno')
        try:
            Infinity.objects.create(
                firstname=firstname,
                lastname=lastname,
                phoneno=phoneno
            )
        except:
            return render(request, 'index.html',{'error':'Exception'})
        
        return render(request, 'index.html',{'success':'Information Saved'})
    else:
        return render(request, 'index.html',{'error':'Some Error Occured'})
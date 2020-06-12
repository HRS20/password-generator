from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'nextgen/home.html')

def password(request):    
    length= int(request.GET.get('length'))
    mypass=''

    characters=list('abcdefghijklmnopqrstucwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('specialchar'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    
    for i in range(length):
        mypass+=random.choice(characters)


    return render(request,'nextgen/password.html',{'password':mypass})

def string(request):
    return HttpResponse('Testing')

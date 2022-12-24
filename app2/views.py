from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Archan(request):
    return HttpResponse('<h1>Archan is a khup chhan boy</h1>')

def shreya(request):
    return HttpResponse('<h1> Archan is innocent guy </h1>')
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Atreya(request):
    return HttpResponse('<marquee><b>Archan is suffering from depression</b></marquee>')
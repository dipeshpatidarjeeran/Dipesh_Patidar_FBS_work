from django.shortcuts import render
from django.http import HttpResponse

def demo2(request):
    return HttpResponse("Hello from demo2 of MyApp2")
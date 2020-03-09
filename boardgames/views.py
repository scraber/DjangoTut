from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Boardgames list</h1>')

def about(request):
    return HttpResponse('<h1>Boardgames about</h1>')

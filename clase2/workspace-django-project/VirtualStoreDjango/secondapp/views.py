from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def saludo(request):
    return HttpResponse("<h1>Welcome to the second app</h1>")

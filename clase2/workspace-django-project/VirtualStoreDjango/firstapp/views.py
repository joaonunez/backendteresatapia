from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def display_saludar(request):
    saludo = "<h1>Saludos Gente</h1>"
    return HttpResponse(saludo)

def display_date(request):
    dt = datetime.datetime.now()
    s = "<b>Fecha y hora:</b>: " + str(dt)
    return HttpResponse(s)
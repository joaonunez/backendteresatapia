from django.contrib import admin
from django.urls import path

from secondapp.views import saludo

urlpatterns = [
    path('saludo/', saludo),
    
]
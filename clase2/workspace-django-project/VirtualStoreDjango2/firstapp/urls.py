from django.contrib import admin
from django.urls import path

from firstapp.views import display, display_data_time

urlpatterns = [
    path('hola/', display),
    path('ahora/', display_data_time)
]
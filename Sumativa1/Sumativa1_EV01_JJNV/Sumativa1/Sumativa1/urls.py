from django.urls import path
from app import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('listar_trabajador/', views.listar_trabajador, name='listar_trabajador'),
    path('agregar_trabajador/', views.agregar_trabajador, name='agregar_trabajador'),
    path('eliminar_trabajador/<int:id>/', views.eliminar_trabajador, name='eliminar_trabajador'),
    path('actualizar_trabajador/<int:id>/', views.actualizar_trabajador, name='actualizar_trabajador'),
]

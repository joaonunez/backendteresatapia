from django.urls import path
from app import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('listarTrabajador/', views.listarTrabajador, name='listarTrabajador'),
    path('agregarTrabajador/', views.agregarTrabajador, name='agregarTrabajador'),
    path('eliminarTrabajador/<int:id>/', views.eliminarTrabajador, name='eliminarTrabajador'),
    path('actualizarTrabajador/<int:id>/', views.actualizarTrabajador, name='actualizarTrabajador'),
]

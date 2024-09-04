from django.shortcuts import render, redirect, get_object_or_404
from .models import Trabajador
from .forms import TrabajadorForm

def inicio(request):
    return render(request, 'templatesApp/inicio.html')

def listar_trabajador(request):
    trabajadores = Trabajador.objects.all()
    return render(request, 'templatesApp/listar_trabajador.html', {'trabajadores': trabajadores})

def agregar_trabajador(request):
    if request.method == 'POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_trabajador')
    else:
        form = TrabajadorForm()
    return render(request, 'templatesApp/agregar.html', {'form': form})

def eliminar_trabajador(request, id):
    trabajador = get_object_or_404(Trabajador, id_trabajador=id)
    trabajador.delete()
    return redirect('listar_trabajador')

def actualizar_trabajador(request, id):
    trabajador = get_object_or_404(Trabajador, id_trabajador=id)
    if request.method == 'POST':
        form = TrabajadorForm(request.POST, instance=trabajador)
        if form.is_valid():
            form.save()
            return redirect('listar_trabajador')
    else:
        form = TrabajadorForm(instance=trabajador)
    return render(request, 'templatesApp/actualizar.html', {'form': form})

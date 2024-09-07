from django.shortcuts import render, redirect, get_object_or_404
from .models import Trabajador
from .forms import TrabajadorForm

def inicio(request):
    return render(request, 'templatesApp/inicio.html')

def listarTrabajador(request):
    trabajadores = Trabajador.objects.all()
    return render(request, 'templatesApp/listarTrabajador.html', {'trabajadores': trabajadores})

def agregarTrabajador(request):
    if request.method == 'POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarTrabajador')
    else:
        form = TrabajadorForm()
    return render(request, 'templatesApp/agregarTrabajador.html', {'form': form})

def eliminarTrabajador(request, id):
    trabajador = get_object_or_404(Trabajador, id_trabajador=id)
    trabajador.delete()
    return redirect('listarTrabajador')

def actualizarTrabajador(request, id):
    trabajador = get_object_or_404(Trabajador, id_trabajador=id)
    if request.method == 'POST':
        form = TrabajadorForm(request.POST, instance=trabajador)
        if form.is_valid():
            form.save()
            return redirect('listarTrabajador')
    else:
        form = TrabajadorForm(instance=trabajador)
    return render(request, 'templatesApp/actualizarTrabajador.html', {'form': form})

from django.shortcuts import render, redirect

# Create your views here.
from models import Reserva
from forms import ReservaForm

def agregarReserva(request):
    form = ReservaForm()
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReservaForm()

    reservas = Reserva.objects.all()
    data = {'form': form, 'reservas': reservas}
    return render(request, 'templatesApp/agregar.html', data)


def eliminarReserva(request, id):
    reserva = Reserva.objects.get(idSolicitud=id)
    reserva.delete()
    return redirect('/')

def actualizarReserva(request, id):
    reserva = Reserva.objects.get(idSolicitud=id)
    form = ReservaForm(instance=reserva)
    if(request.method == 'POST'):
        form = ReservaForm(request.POST, instance = reserva)
        if form.is_valid():
            form.save()
            form = ReservaForm()

    
from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.hotel.forms import ClienteForm, HabitacionForm, ReservacionForm
from apps.hotel.models import Cliente, Habitacion, Reservacion

# Create your views here.

def index_Cliente(request):
    return render(request, 'hotel/Cindex.html')

# Guardar clientes
def cliente_view(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('crear_reservacion')
    else:
        form = ClienteForm()
    return render(request, 'hotel/cliente_form.html', {'form':form})

# Mostrar clientes
def lista_cliente(request):
    cliente = Cliente.objects.all().order_by('id')
    p = {'clientes':cliente}
    return render(request, 'hotel/lista_cliente.html', p)

# Editar clientes
def editar_cliente(request, idCl):
    cliente = Cliente.objects.get(id = idCl)
    if request.method == 'GET':
        form = ClienteForm(instance=cliente)
    else:
        form = ClienteForm(request.POST, instance = cliente)
        if form.is_valid():
            form.save()
        return redirect('ver_cliente')
    return render(request, 'hotel/cliente_form.html', {'form':form})

# Eliminar cliente
def eliminar_cliente(request, idCl):
    cliente = Cliente.objects.get(id = idCl)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_cliente')
    return render(request, 'hotel/eliminar_cliente.html', {'cliente':cliente})

# ----------------------------------------------------------------------------- #

def index_Habitacion(request):
    return render(request, 'hotel/Hindex.html')

# Guardar habitacion
def habitacion_view(request):
    if request.method == 'POST':
        form = HabitacionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Hindex')
    else:
        form = HabitacionForm()
    return render(request, 'hotel/habitacion_form.html', {'form':form})

# Mostrar habitacion
def lista_habitacion(request):
    habitacion = Habitacion.objects.all().order_by('id')
    p = {'habitaciones':habitacion}
    return render(request, 'hotel/lista_habitacion.html', p)

# Editar habitacion
def editar_habitacion(request, idHab):
    habitacion = Habitacion.objects.get(id = idHab)
    if request.method == 'GET':
        form = HabitacionForm(instance=habitacion)
    else:
        form = HabitacionForm(request.POST, instance = habitacion)
        if form.is_valid():
            form.save()
        return redirect('ver_habitacion')
    return render(request, 'hotel/habitacion_form.html', {'form':form})

# Eliminar habitacion
def eliminar_habitacion(request, idHab):
    habitacion = Habitacion.objects.get(id = idHab)
    if request.method == 'POST':
        habitacion.delete()
        return redirect('ver_habitacion')
    return render(request, 'hotel/eliminar_habitacion.html', {'habitacion':habitacion})

# -------------------------------------------------------------------------------------- #

def index_Reservacion(request):
    return render(request, 'hotel/Rindex.html')

# crear reservacion
def reservacion_view(request):
    if request.method == 'POST':
        form = ReservacionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Rindex')
    else:
        form = ReservacionForm()
    return render(request, 'hotel/reservacion_form.html', {'form':form})

# Mostrar Reservaciones
def lista_reservacion(request):
    reservacion = Reservacion.objects.all().order_by('id')
    p = {'reservaciones':reservacion}
    return render(request, 'hotel/lista_reservacion.html', p)

# Editar reservacion
def editar_reservacion(request, idRes):
    reservacion = Reservacion.objects.get(id = idRes)
    if request.method == 'GET':
        form = ReservacionForm(instance=reservacion)
    else:
        form = ReservacionForm(request.POST, instance = reservacion)
        if form.is_valid():
            form.save()
        return redirect('ver_reservacion')
    return render(request, 'hotel/reservacion_form.html', {'form':form})

# Eliminar reservacion
def eliminar_reservacion(request, idRes):
    reservacion = Reservacion.objects.get(id = idRes)
    if request.method == 'POST':
        reservacion.delete()
        return redirect('ver_reservacion')
    return render(request, 'hotel/eliminar_reservacion.html', {'reservacion':reservacion})

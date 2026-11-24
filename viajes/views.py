from django.shortcuts import get_object_or_404, redirect, render
from .forms import ViajeForm
from .models import Viaje


# LISTAR
def listar_viajes(request):
    viajes = Viaje.objects.all()
    return render(request, "viajes/listar.html", {"viajes": viajes})


# CREAR
def crear_viaje(request):
    if request.method == "POST":
        form = ViajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_viajes")
    else:
        form = ViajeForm()
    return render(request, "viajes/form.html", {"form": form, "titulo_pagina": "Crear Nuevo Viaje"})


# EDITAR
def editar_viaje(request, pk):
    viaje = get_object_or_404(Viaje, pk=pk)
    if request.method == "POST":
        form = ViajeForm(request.POST, instance=viaje)
        if form.is_valid():
            form.save()
            return redirect("listar_viajes")
    else:
        form = ViajeForm(instance=viaje)
    return render(
        request, "viajes/form.html", {"form": form, "titulo_pagina": f"Editar Viaje: {viaje.titulo}"}
    )


# ELIMINAR
def eliminar_viaje(request, pk):
    viaje = get_object_or_404(Viaje, pk=pk)
    if request.method == "POST":
        viaje.delete()
        return redirect("listar_viajes")
    return render(request, "viajes/confirmar_eliminar.html", {"viaje": viaje})
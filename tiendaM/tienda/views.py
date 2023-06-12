from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cancion
from .forms import CancionForm


# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')
def canciones(request):
    canciones = Cancion.objects.all()
    print(canciones)
    return render(request, 'canciones/index.html', {'canciones': canciones})
    return render(request, 'canciones/index.html')
def crear(request):
    formulario = CancionForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('canciones')
    return render(request, 'canciones/crear.html', {'formulario':formulario})
def editar(request, id):
    cancion = Cancion.objects.get(id=id)
    formulario = CancionForm(request.POST or None, request.FILES or None, instance=cancion)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('canciones')
    return render(request, 'canciones/editar.html', {'formulario':formulario})

def eliminar(request, id):
    cancion = Cancion.objects.get(id=id)
    cancion.delete()
    return redirect('canciones')
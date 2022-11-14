from django.shortcuts import render
from .models import Producto
from .forms import ContactoForm
# Create your views here.

def home(request):
    #Hacemos las consultas y lo almacenamos en una lista
    productos = Producto.objects.all()
    #Enviamos la lista por un diccionario
    data ={
        'productos':productos,
        'form':ContactoForm
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "mensaje enviado."
        else:
            data["form"] = formulario
    return render(request,'app/home.html',data)


def listar(request):
    return render(request,'app/productos/listar.html')

def agregar_producto(request):
    return render(request,'app/productos/agregar.html')

def login(request):
    return render(request,'app/registros/Login.html')


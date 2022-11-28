from django.shortcuts import render,redirect,get_object_or_404
from .models import Producto,Contacto
from .forms import ContactoForm,ProductoForm,MarcaForm,MensajeForm,CustonCreatUser
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import permission_required

# Create your views here.

def home(request):
    #Hacemos las consultas y lo almacenamos en una lista
    productos = Producto.objects.all().order_by('nombreMarca')

    
    page = request.GET.get('page',1)
    try:
        paginator = Paginator(productos,8)
        productos = paginator.page(page)

    except:
        raise Http404
    #Enviamos la lista por un diccionario
    data ={
        'entity':productos,
        'form':ContactoForm,
        'paginator':paginator
    }
    #verificamos que el metodo de envio sea post
    if request.method == 'POST':
        #despues obtenemos los datos resividos
        formulario = ContactoForm(data=request.POST)
        #si los datos son validos entonce los guardamos
        if formulario.is_valid():
            formulario.save()
            #enviamos un mensaje
            messages.success(request,"Mensaje Enviado Correctamente")
            #sino 
        else:
            #renviamos el formulario
            data["form"] = formulario
    return render(request,'app/home.html',data)



@permission_required('app.add_producto')
def agregar_producto(request):
    data ={
        'form':ProductoForm
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Producto Guardado Correctamente")
        else:
            data["form"] = formulario
    return render(request,'app/productos/agregar.html',data)

@permission_required('app.view_producto')
def listar(request):
    productos = Producto.objects.all()
    page = request.GET.get('page',1)
    try:
        paginator = Paginator(productos,5)
        productos = paginator.page(page)

    except:
        raise Http404

    #Enviamos la lista por un diccionario
    data ={
        'entity':productos,
        'paginator':paginator
    }
    return render(request,'app/productos/listar.html',data)


@permission_required('app.change_producto')
#este recibe una id para poder buscar el elemento a modificar
def modificar(request,id):
# buscamos el registro por medio del id que resibe y el modelo
    producto = get_object_or_404(Producto,id = id)

    #Enviamos la lista por un diccionario
    data ={
        'form':ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        #le instanciamos el id para que modifique el registro correcto
        formulario = ProductoForm(data=request.POST,files=request.FILES,instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado Correctamente")
            return redirect(to='listar')

    return render(request,'app/productos/modificar.html',data)


@permission_required('app.delate_producto')
def eliminar(request,id):
    #Buscamos el registro por el id y lo borramos
    producto = get_object_or_404(Producto,id = id)
    producto.delete()
    messages.success(request,"Eliminado Correctamente")
    return redirect(to='listar')


@permission_required('app.add_marca')
def marca(request):
    productos = Producto.objects.all()
    #Enviamos la lista por un diccionario
    data ={
        'form':MarcaForm
    }
    #verificamos que el metodo de envio sea post
    if request.method == 'POST':
        #despues obtenemos los datos resividos
        formulario = MarcaForm(data=request.POST)
        #si los datos son validos entonce los guardamos
        if formulario.is_valid():
            formulario.save()
            #enviamos un mensaje
            messages.success(request,"Se guardo la marca exitosamente.")
            #sino 
        else:
            #renviamos el formulario
            data["form"] = formulario
    return render(request,'app/productos/marca.html',data)


@permission_required('app.view_contacto')
def lista_mensajes(request):
    mensajes = Contacto.objects.all()

    page = request.GET.get('page',1)
    try:
        paginator = Paginator(mensajes,12)
        mensajes = paginator.page(page)

    except:
        raise Http404
    #Enviamos la lista por un diccionario
    data ={
        'entity':mensajes,
        'paginator':paginator
    }
    return render(request,'app/productos/listar_mensajes.html',data)

@permission_required('app.delate_contacto')
def eliminar_mensaje(request,id):
    #Buscamos el registro por el id y lo borramos
    producto = get_object_or_404(Contacto,id = id)
    producto.delete()
    messages.success(request,"Eliminado Correctamente")
    return redirect(to='list_mensaje')

@permission_required('app.view_contacto')
def ver_mensaje(request,id):
    
    mensaje = get_object_or_404(Contacto,id = id)

    #Enviamos la lista por un diccionario
    data ={
        'form':MensajeForm(instance=mensaje)
    }

    return render(request,'app/productos/Ver_mensaje.html',data)


def registro(request):
    data ={
        'form':CustonCreatUser()
    }

    if request.method == 'POST':
        formulario = CustonCreatUser(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Te has registrado correctamente.")
            return redirect(to="home")
        data["form"] = formulario
    return render(request,'registration/registro.html',data)

@permission_required('app.view_producto')
def inicioAdmin(request):
    return render(request,'app/inicioAdmin.html')
    




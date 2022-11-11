from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    stock = models.IntegerField()
    nombreMarca = models.ForeignKey(Marca,on_delete=models.PROTECT)
    #creamos el campo imagen y le decimos que la imagen la guarde en la carpeta producto y que sea nulo
    imagen = models.ImageField(upload_to="producto", null=True)
    
    def __str__(self):
        return self.nombreProducto

#Creamos las opciuones 
opciones_consulta =[
    [0,"consulta"],
    [1,"reclamo"],
    [2,"sugerencias"],
    [3,"felicitaciones"]
]
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    #creamos el campo en la base de datos y le enviamos las opciones
    tipo_consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre

class Prueba(models.Model):
    nombre = models.CharField(max_length=50)


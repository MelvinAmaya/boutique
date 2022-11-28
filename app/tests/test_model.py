from django.test import TestCase
from app.models import *

class TestModels(TestCase):

    def test_model(self):
        marca = Marca.objects.create( 
            nombre = "prueba2"
        )
        self.Clienteprueba = Producto.objects.create(
            nombreProducto="camisa de juan",
            precio=20,
            descripcion="es una camisa muy grande",
            stock=123,
            nombreMarca= marca,
            
        )

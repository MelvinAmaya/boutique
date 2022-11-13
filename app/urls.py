from django.urls import path
from .views import home,listar,agregar_producto,modificar,eliminar,marca,lista_mensajes,eliminar_mensaje,ver_mensaje

urlpatterns = [
    path('', home,name="home"),
    path('listar/', listar,name="listar"),
    path('agregar/', agregar_producto,name="agregar"),
    path('modificar/<id>/', modificar,name="modificar"),
    path('eliminar/<id>/', eliminar,name="eliminar"),
    path('marca/', marca,name="marca"),
    path('listar-mensaje/', lista_mensajes,name="list_mensaje"),
    path('eliminar_mensaje/<id>/', eliminar_mensaje,name="delate_mesaje"),
    path('verMensaje/<id>/', ver_mensaje,name="see_mesaje"),
]
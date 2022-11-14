from django.urls import path
from .views import home,listar,agregar_producto,login

urlpatterns = [
    path('', home,name="home"),
    path('listar/', listar,name="listar"),
    path('agregar/', agregar_producto,name="agregar"),
    path('login/', login, name="login")
]
from django.contrib import admin
from .models import Marca,Producto,Contacto
# Register your models here.

#Para personalizar el admin
class ProductoAdmin(admin.ModelAdmin):
    #filtros
    list_display = ["nombreProducto","precio","stock","nombreMarca"]
    list_editable = ["precio"]
    search_fields = ["nombreProducto"]
    list_filter = ["nombreMarca"]
    list_per_page = 10

#registramos los modelos en el admin
admin.site.register(Marca)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Contacto)

from django import forms
from .models import Contacto,Producto,Marca,Contacto

#Creamos una clase que hereda de forms
class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        #damos a entender que todos los camos del modelos seran los mosmos que este
        fields = '__all__'

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

class MarcaForm(forms.ModelForm):

    class Meta:
        model = Marca
        fields = '__all__'

class MensajeForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'
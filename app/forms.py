from django import forms
from .models import Contacto

#Creamos una clase que hereda de forms
class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        #damos a entender que todos los camos del modelos seran los mosmos que este
        fields = '__all__'
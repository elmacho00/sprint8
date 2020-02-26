from django import forms
from .models import *
from django import forms

class ProduForm(forms.ModelForm):
    class Meta:
        model= Producto
        fields = ['nombre', 'precio', 'descripcion', 'stock']
        labels = {
            'nombre':'Nombre de Producto', 
            'precio': 'Precio', 
            'descripcion':'Descripcion',
            'stock':'stock',
            
            }

from django.forms import ModelForm
from .models import Pedidos

class pedidoForm(ModelForm):
    class Meta:
        model = Pedidos
        fields = ['rut','nombre','apellido','telefono','email','descripcion']
    
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pedidos(models.Model):
    rut = models.CharField(max_length=25)
    nombre = models.CharField(max_length=25)
    apellido =models.CharField(max_length=25)
    telefono =models.CharField(max_length=25)
    email = models.EmailField()
    fecha_comienzo = models.DateTimeField(auto_now_add=True)
    fecha_termino = models.DateTimeField(null=True, blank=True)
    cobro = models.CharField(max_length=5)
    estado_del_cobro = models.BooleanField(default=False)
    descripcion = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.rut + ' --- '+'Usuario: '+ self.user.username
 
class finanzas(models.Model):
    gastos = models.CharField(max_length=10)
    ganancias = models.ForeignKey(Pedidos, on_delete=models.RESTRICT)
    descripcion = models.TextField(blank=True)
    
    
class inventario(models.Model):
    herramientas = models.CharField(max_length=25)
    stock = models.CharField(max_length=3)
    descripcion = models.TextField(blank=True)
    
    
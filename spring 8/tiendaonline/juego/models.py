from django.db import models


    
class Usuario (models.Model):
    nombreUsu = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=50,null=True)

class Carrito (models.Model):
    nombreProducto = models.CharField(max_length=50,null=True)
    precioProducto = models.IntegerField(default=10,null=True)
    cantidad = models.IntegerField(default=0,null=True)

class Producto(models.Model):
    nombre = models.CharField(max_length=50,null=True)
    precio = models.IntegerField(default=10,null=True)
    descripcion = models.CharField(max_length=500,null=True)
    stock = models.IntegerField(default=100,null=True)
    carrito1 = models.ForeignKey(Carrito,on_delete = models.CASCADE, null = True)
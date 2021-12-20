from django.db import models

# Create your models here.
class Sedes(models.Model):
    id = models.AutoField (primary_key = True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField(null=True, blank=True)	

class Horarios(models.Model):
    id = models.AutoField (primary_key = True)
    sedes = models.ForeignKey(Sedes, on_delete=models.SET_NULL, null=True)
    dia = models.CharField(max_length=32)
    hora_inicio = models.IntegerField(null=True, blank=True)
    hora_fin = models.IntegerField(null=True, blank=True)

class Planes(models.Model):
    id = models.AutoField (primary_key = True)
    nombre = models.CharField(max_length=32)
    tiempo = models.IntegerField(null=True, blank=True)
    valor = models.DecimalField(max_digits=6, decimal_places=2)

class Categorias(models.Model):
    id = models.AutoField (primary_key = True)
    nombre = models.CharField(max_length=100)

class Rutinas(models.Model):
    id = models.AutoField (primary_key = True)
    categorias = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True)
    descripcion = models.CharField(max_length=100)
    
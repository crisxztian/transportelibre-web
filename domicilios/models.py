from django.db import models


usuariosauth=(
(0,'invalidado'),
(1,'validado'),
)

moviles=(
(0,'Moto'),
(1,'Carro'),
(2,'Camión'),
)

class domiciliarios(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.TextField()
    apellidos = models.TextField()
    email = models.TextField()
    clave = models.TextField()
    estado = models.CharField(choices=usuariosauth, max_length=10, default='invalidado')
    telefono = models.TextField()
    documento = models.TextField()
    reputacion = models.IntegerField()
    rostro = models.FileField()

class clientes(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.TextField()
    apellidos = models.TextField()
    email = models.TextField()
    clave = models.TextField()
    estado = models.CharField(choices=usuariosauth, max_length=10, default='invalidado')
    telefono = models.TextField()
    direccion = models.TextField(blank=True)

class vehiculos(models.Model):
    id= models.AutoField(primary_key=True)
    tipo = models.CharField(choices=moviles, max_length=8)
    placa = models.CharField(max_length=7)
    domiciliarios = models.ForeignKey('domiciliarios')

from django.db import models

# Create your models here.

from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    rut = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=255)
    direccion = models.CharField(max_length=255)
    creado = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=255)

class Mascota(models.Model):
    nombre = models.CharField(max_length=255)
    especie = models.CharField(max_length=255)
    raza = models.CharField(max_length=255)
    sexo = models.CharField(max_length=10)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    edad = models.IntegerField()

class MedicoVeterinario(models.Model):
    nombre = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=255)
    correo = models.EmailField(max_length=255)
    telefono = models.CharField(max_length=20)

class Cita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    medico = models.ForeignKey(MedicoVeterinario, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()
    confirmada = models.BooleanField(default=False)

# ADMIN
class Administrador(models.Model):
    correo = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


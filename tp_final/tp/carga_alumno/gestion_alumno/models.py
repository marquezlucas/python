from django.db import models

# Create your models here.

class BandaHoraria(models.Model):
    nombre = models.CharField(max_length=255)
    horario_inicio = models.DateTimeField()
    horario_fin = models.DateTimeField()

class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    banda_horaria = models.ForeignKey(BandaHoraria, on_delete=models.CASCADE)
    nota = models.IntegerField()

class Alumno(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    dni = models.CharField(primary_key=True, max_length=255)
    telefono = models.CharField(max_length=255)
    correo_electronico = models.EmailField()
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
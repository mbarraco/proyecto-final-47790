from django.db import models

## CLASE 24
from django.contrib.auth.models import User

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.FileField(upload_to="media/avatares", null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    profesion = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.appelido}"


class Curso(models.Model):
    curso = models.CharField(max_length=30)
    camada = models.IntegerField()

    def __str__(self):
        return f"{self.curso} ({self.camada})"
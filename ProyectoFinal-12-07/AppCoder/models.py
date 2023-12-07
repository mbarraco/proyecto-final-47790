from django.db import models


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
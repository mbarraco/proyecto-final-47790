from django.db import models


class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()

class Curso(models.Model):
    curso = models.CharField(max_length=30)
    camada = models.IntegerField()

    def __str__(self):
        return f"{self.curso} ({self.camada})"
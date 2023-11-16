from django.shortcuts import render
from django.http import HttpResponse


def inicio_view(xx):
    return HttpResponse("Bienvenidos!!!!!!!!!!!!!!")


def cursos_view(xx):
    # return HttpResponse("Aquí voy a mostrar mis cursos")
    return render(xx, "AppCoder/padre.html")
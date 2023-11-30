from django.shortcuts import render
from django.http import HttpResponse


def inicio_view(xx):
    return HttpResponse("Bienvenidos!!!!!!!!!!!!!!")


from django.template import Template, Context
from django.http import HttpResponse
from datetime import datetime

def xx_cursos_view(xx):
    # return HttpResponse("Aquí voy a mostrar mis cursos")
    return render(xx, "AppCoder/padre.html")



def cursos_view(xx): # en las slides es `probandoTemplate``
    nombre = "Mariano Manuel"
    apellido = "Barracovich"
    ahora = datetime.now()
    diccionario = {
        'nombre': nombre,
        'apellido': apellido,
        "nacionalidad": "argentino",
        "hora": ahora,
        "ciudades_preferidas": ["Buenos Aires", "Lima", "San Pablo", "Trieste"]
    }  # Para enviar al contexto

    ruta = "/Users/marianobarraco/code/proyecto-final-47790/ProyectoFinal-2/AppCoder/templates/AppCoder/padre.html"
    mi_archivo = open(ruta, "r")
    # "Método django - versión 1"
    plantilla = Template(mi_archivo.read())  # Se carga en memoria nuestro documento, template1
    contexto = Context(diccionario)  # Le doy al contexto mi nombre y apellido
    documento = plantilla.render(contexto)  # Aqui renderizamos la plantilla en documento

    return HttpResponse(documento)


def profesores_view(xx):
    nombre = "Mariano Manuel"
    apellido = "Barracovich"
    ahora = datetime.now()
    diccionario = {
        'nombre': nombre,
        'apellido': apellido,
        "nacionalidad": "argentino",
        "hora": ahora,
        "ciudades_preferidas": ["Buenos Aires", "Lima", "San Pablo", "Trieste"]
    }  # Para enviar al contexto
    return render(xx, "AppCoder/padre.html", diccionario)
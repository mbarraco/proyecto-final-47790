from django.shortcuts import render
from django.http import HttpResponse


def inicio_view(xx):
    return HttpResponse("Bienvenidos!!!!!!!!!!!!!!")


from django.template import Template, Context
from django.http import HttpResponse


def xx_cursos_view(xx):
    # return HttpResponse("Aquí voy a mostrar mis cursos")
    return render(xx, "AppCoder/padre.html")



def cursos_view(xx):
    nom = "Nicolas"
    ap = "Perez"

    diccionario = {'nombre': nom, 'apellido': ap}  # Para enviar al contexto

    # Assuming 'template1.html' is in the correct directory.
    with open("/Users/marianobarraco/code/proyecto-final-47790/ProyectoFinal-2/AppCoder/templates/AppCoder/padre.html") as miHtml:
        plantilla = Template(miHtml.read())  # Se carga en memoria nuestro documento, template1

    # Crear el contexto con el diccionario
    miContexto = Context(diccionario)  # Le doy al contexto mi nombre y apellido

    # Renderizar la plantilla con el contexto
    documento = plantilla.render(miContexto)  # Aqui renderizamos la plantilla en documento

    return HttpResponse(documento)

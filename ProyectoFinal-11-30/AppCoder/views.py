from datetime import date

from django.shortcuts import redirect, render

from datetime import datetime
from . import models
from .models import Curso

from .forms import CursoFormulario, CursoBuscarFormulario


def inicio_view(request):
    return render(request, "AppCoder/inicio.html")


def cursos_buscar_view(request):
    if request.method == "GET":
        form = CursoBuscarFormulario()
        return render(
            request,
            "AppCoder/curso_formulario_busqueda.html",
            context={"form": form}
        )
    else:
        formulario = CursoBuscarFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            cursos_filtrados = []
            for curso in Curso.objects.filter(curso=informacion["curso"]):
                cursos_filtrados.append(curso)

            contexto = {"cursos": cursos_filtrados}
            return render(request, "AppCoder/cursos_list.html", contexto)


def cursos_todos_view(request):
    todos_los_cursos = []
    for curso in Curso.objects.all():
        todos_los_cursos.append(curso)

    contexto = {"cursos": todos_los_cursos}
    return render(request, "AppCoder/cursos_list.html", contexto)


def cursos_view(request):
    if request.method == "GET":
        print("+" * 90) #  Imprimimos esto para ver por consola
        print("+" * 90) #  Imprimimos esto para ver por consola
        form = CursoFormulario()
        return render(
            request,
            "AppCoder/curso_formulario_avanzado.html",
            context={"form": form}
        )
    else:
        formulario = CursoFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = Curso(curso=informacion["curso"], camada=informacion["camada"])
            modelo.save()

        return redirect("AppCoder:inicio")


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



# Tomado de la clase dad por Esteban
def crear_clientes_varios(request):
    p1 = models.Pais(nombre="Paraguay")
    p2 = models.Pais(nombre="México")
    p3 = models.Pais(nombre="El Salvador")
    p1.save()
    p2.save()
    p3.save()
    c1 = models.Cliente(nombre="Almendra", apellido="Ruiseñor", nacimiento=date(2015, 1, 1), pais_origen=p1)
    c2 = models.Cliente(nombre="Giordana", apellido="Tapello", nacimiento=date(2005, 2, 2), pais_origen=p2)
    c3 = models.Cliente(nombre="Macarena", apellido="Lito", nacimiento=date(1990, 1, 1), pais_origen=p3)
    c4 = models.Cliente(nombre="Jhiordana", apellido="Perez", nacimiento=date(2005, 1, 1), pais_origen=None)
    c1.save()
    c2.save()
    c3.save()
    c4.save()
    return redirect("AppCoder:inicio")
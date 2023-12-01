from django.urls import path

from AppCoder.views import cursos_view, cursos_buscar_view, cursos_todos_view, inicio_view, profesores_view, crear_clientes_varios

app_name = "AppCoder"

urlpatterns = [
    path("cursos/", cursos_view, name="cursos"),
    path("cursos/todos", cursos_todos_view, name="cursos-todos"),
    path("cursos/buscar", cursos_buscar_view, name="cursos-buscar"),
    path("comisiones/", profesores_view),
    path("crear_clientes_varios/", crear_clientes_varios),
    path("inicio/", inicio_view, name="inicio"),
    path("inicio/", inicio_view, name="inicio"),
]

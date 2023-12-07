from django.urls import path

from AppCoder.views import (
    cursos_view,
    cursos_buscar_view,
    cursos_todos_view,
    inicio_view,
    profesores_view,
    ### CRUD
    profesores_crud_delete_view,
    profesores_crud_read_view,
    profesores_crud_update_view,
    profesor_view,
    CursoCreateView,
    CursoDetail,
    CursoDeleteView,
    CursoListView,
    CursoUpdateView,
    )


app_name = "AppCoder"

urlpatterns = [
    path("cursos/", cursos_view, name="cursos"),
    path("cursos/todos", cursos_todos_view, name="cursos-todos"),
    path("cursos/buscar", cursos_buscar_view, name="cursos-buscar"),
    path("comisiones/", profesores_view),
    path("inicio/", inicio_view, name="inicio"),
    ###### CRUD
    path("profesores/", profesor_view),
    path("profesores-lista/", profesores_crud_read_view),
    path("profesores-eliminar/<profesor_email>/", profesores_crud_delete_view),
    path("profesores-editar/<profesor_email>/", profesores_crud_update_view),
    ###### CBV
    ### CBV
    path("curso/list", CursoListView.as_view(), name="curso-list"),
    path("curso/new", CursoCreateView.as_view(), name="curso-create"),
    path("curso/<pk>", CursoDetail.as_view(), name="curso-detail"),
    path("curso/<pk>/update", CursoUpdateView.as_view(), name="curso-update"),
    path("curso/<pk>/delete", CursoDeleteView.as_view(), name="curso-delete"),

]

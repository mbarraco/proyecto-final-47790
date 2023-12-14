from django.urls import path
from django.contrib.auth.views import LogoutView

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
    ### LOGIN
    login_view,
    registro_view,
    ### EDITAR PERFIL
    editar_perfil_view,
    crear_avatar_view,
    ### INSTRAGRAM
    mostrar_profile_view,
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
    path("curso/list", CursoListView.as_view(), name="curso-list"),
    path("curso/new", CursoCreateView.as_view(), name="curso-create"),
    path("curso/<pk>", CursoDetail.as_view(), name="curso-detail"),
    path("curso/<pk>/update", CursoUpdateView.as_view(), name="curso-update"),
    path("curso/<pk>/delete", CursoDeleteView.as_view(), name="curso-delete"),
    ###### LOGIN
    path("registro", registro_view, name="registro"),
    path("login", login_view, name="login"),
    path("logout", LogoutView.as_view(template_name="AppCoder/logout.html"), name="logout"),
    ###### EDITAR USUARIO
    path("editar-perfil", editar_perfil_view, name="editar-perfil"),
    path("crear-avatar", crear_avatar_view, name="crear-avatar"),
    ##### INSTRAGAM
    path("profile/<user_id>", mostrar_profile_view, name="profile"),
]

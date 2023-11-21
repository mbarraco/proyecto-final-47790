from django.urls import path
from django.http import HttpResponse

from AppCoder.views import cursos_view, inicio_view


urlpatterns = [
    path("cursos/", cursos_view),  # "cursos_view" atiende en esta ruta
    path("inicio/", inicio_view),
]

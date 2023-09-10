from django.urls import path
from .views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-cursos/', listar_cursos),
    path('', inicio, name="Inicio"),
    path('cursos/', cursos, name="Cursos"),
    path('profesores/', profesores, name="Profesores"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('entregables/', entragables, name="Entregables"),
    path('curso-formulario/', cursoFormulario, name="CursoFormulario"),
    ]

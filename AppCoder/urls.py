from django.urls import path
from .views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-cursos/', listar_cursos, name = 'ListaCursos'),
    path('', inicio, name="Inicio"),
    path('cursos/', cursos, name="Cursos"),
    path('profesores/', profesores, name="Profesores"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('entregables/', entragables, name="Entregables"),
    path('curso-formulario/', cursoFormulario, name="CursoFormulario"),
    path('profesores-formulario/', profesoresFormulario, name="ProfesoresFormulario"),
    path('busqueda-camada/', busquedaCamada, name="BusquedaCamada"),
    path('buscar/', buscar, name="Buscar"),
    ]

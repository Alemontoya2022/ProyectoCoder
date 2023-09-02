from django.contrib import admin
from django.urls import path
from AppCoder.views import curso, listar_cursos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-cursos/', listar_cursos),
]

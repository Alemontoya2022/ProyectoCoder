from django.contrib import admin
from django.urls import path, include
from AppCoder.views import curso, listar_cursos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app-coder/',include('AppCoder.urls'))
]

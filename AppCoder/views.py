from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Curso, Profesor
from .forms import CursoFormulario, ProfesoresFormulario


def curso(req, nombre, camada):
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()

    return HttpResponse(f"""
    <p>---->Curso: {curso.nombre} Camada: {curso.camada} creado con exito!</p>
    """)

    
def listar_cursos(req):

    lista = Curso.objects.all()

    return render(req, "lista_cursos.html", {"lista_cursos": lista})
 
def inicio(req):

    return render(req, "inicio.html")
    

def cursos(req):

     return render(req, "cursos.html")

def profesores(req):

    return render(req, "profesores.html")

def estudiantes(req):

    return render(req, "estudiantes.html")

def entragables(req):

    return render(req, "entregables.html")

def cursoFormulario(req):
    
    print('method', req.method)
    print('POST', req.POST) # se puede sacar de aca el curso y camada, como esta hecho abajo lo hacemos a traves de django para poner ciertas "restricciones" a los valores de entrrada de campo, desde el forms.py creando def 

    if req.method == "POST":
    
        miFormulario = CursoFormulario(req.POST)

        if miFormulario.is_valid(): #<----------------- ESTO ES LO CLAVE DE DJANGO

            data = miFormulario.cleaned_data
            curso = Curso(nombre=data["curso"], camada=data["camada"])
            curso.save()

        return render(req, "inicio.html")
         
    else:
        miFormulario = CursoFormulario()    
        return render(req, "cursoFormulario.html", {"miFormulario" : miFormulario })
    

def profesoresFormulario(req):
    
    print('method', req.method)
    print('POST', req.POST) # se puede sacar de aca el curso y camada, como esta hecho abajo lo hacemos a traves de django para poner ciertas "restricciones" a los valores de entrrada de campo, desde el forms.py creando def 

    if req.method == "POST":
    
        miFormulario = ProfesoresFormulario(req.POST)

        if miFormulario.is_valid(): #<----------------- ESTO ES LO CLAVE DE DJANGO

            data = miFormulario.cleaned_data
            profesores = Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], profesion=data["profesion"])
            profesores.save()

        return render(req, "inicio.html")
         
    else:
        miFormulario = ProfesoresFormulario()    
        return render(req, "ProfesoresFormulario.html", {"miFormulario" : miFormulario })


def busquedaCamada(req):

    return render(req, "busquedaCamada.html")

def buscar(req: HttpRequest):

    if req.GET["camada"]:
            camada = req.GET["camada"]
            cursos =  Curso.objects.filter(camada__icontains=camada)       
            return render(req, "resultadosBusqueda.html", {"cursos" : cursos })
    else:
      return HttpResponse(f"Debe agregar una camada")
    
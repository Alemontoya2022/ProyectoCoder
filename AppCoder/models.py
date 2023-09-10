from django.db import models

class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    fecha_creacion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} - {self.camada}'
    
        
    class Meta():
        verbose_name = 'Course'
        verbose_name_plural = 'The Courses'
        ordering = ('nombre' ,'-camada') #PARA DEFINIR UNA TUPLA DE UN UNICO ELEMENTO DEBEMOS PONERLE UNA COMA AL FINAL, SINO SERIA UN STR
        unique_together = ('nombre', 'camada') #no puedo crear un curso que ya erxiste

class Estudiante(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre} - {self.apellido}'

class Profesor(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion= models.CharField(max_length=30)


    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.email} - {self.profesion}'
    
class Entregable(models.Model):

    nombre = models.CharField(max_length=40)
    FechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    link = models.CharField(max_length=256, null=True)
    estudiante= models.ForeignKey(Estudiante, on_delete=models.CASCADE)#COMO ACTUALIZAMOS EL MODELO, LO TENEMOS DEFASADO DEL DB SQLITE HAY QUE MIGRARLO CON EL MAKEMIGRATONS







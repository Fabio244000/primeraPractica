from django.db import models

#creando las clases EDITO, AUTOR, LIBRO
class Editor(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=60)
    estado = models.CharField(max_length=30)
    pais = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["nombre"]

    def __str__(self): # __unicode__ en Python 2
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e­mail')

    

    def __str__(self): # __unicode__ en Python 2
        return '%s %s' % (self.nombre, self.apellidos)
    

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE,)
    fecha_publicacion = models.DateField(blank=True, null=True)
    portada = models.ImageField(upload_to='portadas')


    def __str__(self): # __unicode__ en Python 2
        return self.titulo
# Create your models here.

from django.db import models

# Create your models here.

class Profesor(models.Model):
    rut = models.CharField(max_length=9, null=False, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo = models.BooleanField(default=True)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50, null=False, blank=False)

class Curso(models.Model):
    codigo = models.CharField(unique=True, max_length=10, primary_key=True, null=False)
    nombre = models.CharField(max_length=50, null=False)
    version = models.IntegerField(null=False)
    profesor_id = models.ManyToManyField("Profesor", verbose_name="Profesor", related_name='cursos')
    estudiante_id = models.ManyToManyField("Estudiante", verbose_name="Estudiante", related_name='cursos')

class Estudiante(models.Model):
    rut = models.CharField(max_length=9, null=False, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    fecha_nac = models.DateField(null=False, blank=False)
    activo = models.BooleanField(default=True)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50, null=False, blank=False)

class Direccion(models.Model):
    calle = models.CharField(max_length=50, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    dpto = models.CharField(max_length=10, null=True, blank=True)
    comuna = models.CharField(max_length=50, null=False, blank=False)
    ciudad = models.CharField(max_length=50, null=False, blank=False)
    region = models.CharField(max_length=50, null=False, blank=False)
    estudiante_id = models.OneToOneField("Estudiante", verbose_name="Estudiante", null=False, blank=False, on_delete=models.CASCADE)
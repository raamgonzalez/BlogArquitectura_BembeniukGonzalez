from distutils.command.upload import upload
from django.db import models

class Obra_arq(models.Model):
    nombre_obra = models.CharField(max_length=100)
    ubicacion_obra = models.CharField(max_length=100,null=True)
    año = models.IntegerField(null=True)
    tipo = models.CharField(max_length=100, null=True)
    descripcion = models.CharField(max_length=300)
    arquitecto = models.ForeignKey('Arquitecto', on_delete = models.CASCADE, related_name='obras')
    image = models.ImageField(upload_to = 'obras', default = 'default.png')

    class Meta:
        verbose_name = 'Obra de Arquitectura'
        verbose_name_plural = 'Obras de Arquitectura'

    def __str__(self):
        return self.nombre_obra

class Arquitecto(models.Model):
    nombre_apellido_arqui = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    image = models.ImageField(upload_to = 'arquitectos',  default = 'default.png')

    class Meta:
        verbose_name = 'Arquitecto'
        verbose_name_plural = 'Arquitectos'

    def __str__(self):
        return self.nombre_apellido_arqui

from django.db import models

class Obra_arq(models.Model):
    nombre_obra = models.CharField(max_length=100)
    autor_obra = models.CharField(max_length=100, unique=True)
    ubicacion_obra = models.CharField(max_length=100,null=True)
    año = models.IntegerField(null=True)
    tipo = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Obra de Arquitectura'
        verbose_name_plural = 'Obras de Arquitectura'

class Inst_edu(models.Model):
    nombre_inst = models.CharField(max_length=100)
    ubicacion_inst = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Institución educativa'
        verbose_name_plural = 'Instituciones educativas'

class Bibliografia(models.Model):
    nombre_biblio = models.CharField(max_length=100)
    autor_biblio = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Bibliografia'
        verbose_name_plural = 'Bibliografias'
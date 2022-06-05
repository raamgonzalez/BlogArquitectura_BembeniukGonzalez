from django.db import models

class Obra_arq(models.Model):
    nombre_obra = models.CharField(max_length=100)
    autor_obra = models.CharField(max_length=100, unique=True)
    ubicacion_obra = models.CharField(max_length=100,null=True)
    año = models.IntegerField(null=True)
    tipo = models.CharField(max_length=100, null=True)

class Inst_edu(models.Model):
    nombre_inst = models.CharField(max_length=100)
    ubicacion_inst = models.CharField(max_length=100)

class Bibliografia(models.Model):
    nombre_biblio = models.CharField(max_length=100)
    autor_biblio = models.CharField(max_length=100)
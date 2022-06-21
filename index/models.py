from django.db import models

# Create your models here.
class Titulos(models.Model):
    contenido = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Titulos'
        verbose_name_plural = 'Titulos'

    def __str__(self):
        return self.contenido
    
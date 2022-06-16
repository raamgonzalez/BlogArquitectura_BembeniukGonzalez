from django.contrib import admin

from app_blog.models import Arquitecto, Obra_arq

# Register your models here.
@admin.register(Obra_arq)
class Obra_arq(admin.ModelAdmin):
    list_display = ['nombre_obra','tipo']

@admin.register(Arquitecto)
class Arquitecto(admin.ModelAdmin):
    list_display = ['nombre_arqui','apellido_arqui']
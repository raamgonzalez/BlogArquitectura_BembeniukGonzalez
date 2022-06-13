from django.contrib import admin

from app_blog.models import Bibliografia, Inst_edu, Obra_arq

# Register your models here.
@admin.register(Obra_arq)
class Obra_arq(admin.ModelAdmin):
    list_display = ['nombre_obra','autor_obra','tipo']

@admin.register(Inst_edu)
class Inst_edu(admin.ModelAdmin):
    list_display = ['nombre_inst','ubicacion_inst']

@admin.register(Bibliografia)
class Bibliografia(admin.ModelAdmin):
    list_display = ['nombre_biblio','autor_biblio']
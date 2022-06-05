from django.contrib import admin

from app_blog.models import Bibliografia, Inst_edu, Obra_arq

# Register your models here.
admin.site.register(Obra_arq)
admin.site.register(Inst_edu)
admin.site.register(Bibliografia)
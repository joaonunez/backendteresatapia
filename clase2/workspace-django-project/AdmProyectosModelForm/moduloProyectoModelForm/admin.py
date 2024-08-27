from django.contrib import admin

# Register your models here.
from .models import Proyecto

class ProyectoAdmin(admin.ModelAdmin):
    list_display=['fechaInicio',
                 'fechaTermino',
                 'nombre',
                 'responsable',
                 'prioridad'
                 ]

admin.site.register(Proyecto, ProyectoAdmin)
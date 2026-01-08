from django.contrib import admin
from .models import Alumno, Profesor, Curso, Inscripcion


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = (
        'cedula',
        'nombres',
        'apellidos',
        'correo',
        'telefono',
    )
    search_fields = ('cedula', 'nombres', 'apellidos')
    list_filter = ('nombres', 'apellidos')
    ordering = ('apellidos',)

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = (
        'cedula',
        'nombres',
        'apellidos',
        'correo',
        'telefono',
    )
    search_fields = ('nombres', 'apellidos', 'cedula')
    list_filter = ('nombres', 'apellidos')
    ordering = ('apellidos',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'idioma',
        'nivel',
    )
    list_filter = ('idioma', 'nivel')
    search_fields = ('nombre',)
    ordering = ('nivel',)

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):


    list_display = (
        'fecha_inscripcion',
        'abono_propio',
        'abono_inscripcion'
    )
    list_filter = ('fecha_inscripcion', 'abono_inscripcion')
    search_fields = (
        'fecha_inscripcion',
        'abono_propio',
    )
    ordering = ('fecha_inscripcion',)


admin.site.site_header = "Instituto BrentWood"
admin.site.site_title = "Administración Del Instituto BrentWood"
admin.site.index_title = "Panel de Gestión Académica"

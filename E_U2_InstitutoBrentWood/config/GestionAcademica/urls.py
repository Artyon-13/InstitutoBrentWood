from django.urls import path

from . import views


urlpatterns = [
    path('alumnos/', views.alumnos_view, name='alumnos'),
    path('profesores/', views.profesores_view, name='profesores'),
    path('cursos/', views.cursos_view, name='cursos'),
    path('inscripciones/', views.inscripciones_view, name='inscripciones'),
]


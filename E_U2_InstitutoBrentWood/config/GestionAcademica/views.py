from django.shortcuts import render, redirect
from bson import ObjectId

from .models import Alumno, Profesor, Curso, Inscripcion
from .forms import (
    AlumnoForm,
    ProfesorForm,
    CursoForm,
    InscripcionForm
)


# =========================
# ALUMNOS (LISTAR + CREAR)
# =========================
def alumnos_view(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            Alumno.objects.create(
                cedula=form.cleaned_data['cedula'],
                nombres=form.cleaned_data['nombres'],
                apellidos=form.cleaned_data['apellidos'],
                telefono=form.cleaned_data['telefono'],
                direccion=form.cleaned_data['direccion'],
                correo=form.cleaned_data['correo'],
                edad=form.cleaned_data['edad']
            )
            return redirect('alumnos')
    else:
        form = AlumnoForm()

    alumnos = Alumno.objects.all()

    return render(request, 'academia/alumno_form.html', {
        'form': form,
        'alumnos': alumnos
    })


# =========================
# PROFESORES (LISTAR + CREAR)
# =========================
def profesores_view(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            Profesor.objects.create(
                cedula=form.cleaned_data['cedula'],
                nombres=form.cleaned_data['nombres'],
                apellidos=form.cleaned_data['apellidos'],
                telefono=form.cleaned_data['telefono'],
                direccion=form.cleaned_data['direccion'],
                correo=form.cleaned_data['correo']
            )
            return redirect('profesores')
    else:
        form = ProfesorForm()

    profesores = Profesor.objects.all()

    return render(request, 'academia/profesor_form.html', {
        'form': form,
        'profesores': profesores
    })


# =========================
# CURSOS (LISTAR + CREAR)
# =========================
def cursos_view(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            profesor = Profesor.objects.get(
                id=ObjectId(form.cleaned_data['profesor'])
            )

            Curso.objects.create(
                nombre=form.cleaned_data['nombre'],
                idioma=form.cleaned_data['idioma'],
                nivel=form.cleaned_data['nivel'],
                profesor=profesor
            )
            return redirect('cursos')
    else:
        form = CursoForm()

    cursos = Curso.objects.all()

    return render(request, 'academia/curso_form.html', {
        'form': form,
        'cursos': cursos
    })


# =========================
# INSCRIPCIONES (LISTAR + CREAR)
# =========================
def inscripciones_view(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            alumno = Alumno.objects.get(
                id=ObjectId(form.cleaned_data['alumno'])
            )
            curso = Curso.objects.get(
                id=ObjectId(form.cleaned_data['curso'])
            )

            Inscripcion.objects.create(
                fecha_inscripcion=form.cleaned_data['fecha_inscripcion'],
                abono_propio=form.cleaned_data['abono_propio'],
                abono_inscripcion=form.cleaned_data['abono_inscripcion'],
                alumno=alumno,
                curso=curso
            )
            return redirect('inscripciones')
    else:
        form = InscripcionForm()

    inscripciones = Inscripcion.objects.all()

    return render(request, 'academia/inscripcion_form.html', {
        'form': form,
        'inscripciones': inscripciones
    })





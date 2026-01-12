from django import forms
from .models import Alumno, Profesor, Curso


# =========================
# ALUMNO
# =========================
class AlumnoForm(forms.Form):
    cedula = forms.CharField(max_length=10)
    nombres = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    telefono = forms.CharField(max_length=10, required=False)
    direccion = forms.CharField(max_length=100, required=False)
    correo = forms.EmailField()
    edad = forms.IntegerField()


# =========================
# PROFESOR
# =========================
class ProfesorForm(forms.Form):
    cedula = forms.CharField(max_length=10)
    nombres = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    telefono = forms.CharField(required=False)
    direccion = forms.CharField(required=False)
    correo = forms.EmailField()


# =========================
# CURSO
# =========================
class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    idioma = forms.CharField(max_length=30)
    nivel = forms.CharField(max_length=30)
    profesor = forms.ChoiceField(label='Profesor')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profesor'].choices = [
            (str(p.id), f"{p.nombres} {p.apellidos}")
            for p in Profesor.objects.all()
        ]


# =========================
# INSCRIPCIÓN
# =========================
class InscripcionForm(forms.Form):
    fecha_inscripcion = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    abono_propio = forms.BooleanField(required=False)
    abono_inscripcion = forms.DecimalField(max_digits=8, decimal_places=2)

    alumno = forms.ChoiceField(label='Alumno')
    curso = forms.ChoiceField(label='Curso')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['alumno'].choices = [
            (str(a.id), f"{a.nombres} {a.apellidos}")
            for a in Alumno.objects.all()
        ]
        self.fields['curso'].choices = [
            (str(c.id), c.nombre)
            for c in Curso.objects.all()
        ]


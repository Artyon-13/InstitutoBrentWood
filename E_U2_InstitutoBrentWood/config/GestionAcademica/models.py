from mongoengine import (
    Document,
    StringField,
    IntField,
    EmailField,
    BooleanField,
    DateField,
    DecimalField,
    ReferenceField
)
from datetime import date


class Alumno(Document):
    cedula = StringField(required=True, unique=True, max_length=10)
    nombres = StringField(required=True, max_length=50)
    apellidos = StringField(required=True, max_length=50)
    telefono = StringField(max_length=10)
    direccion = StringField(max_length=100)
    correo = EmailField(required=True, unique=True)
    edad = IntField(required=True)

    meta = {
        'collection': 'Alumno'
    }

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.cedula})"


class Profesor(Document):
    cedula = StringField(required=True, unique=True, max_length=10)
    nombres = StringField(required=True, max_length=50)
    apellidos = StringField(required=True, max_length=50)
    telefono = StringField(max_length=10)
    direccion = StringField(max_length=200)
    correo = EmailField(required=True, unique=True)

    meta = {
        'collection': 'Profesor'
    }

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.cedula})"


class Curso(Document):
    nombre = StringField(required=True, max_length=50)
    idioma = StringField(required=True, max_length=30)
    nivel = StringField(required=True, max_length=30)

    profesor = ReferenceField(Profesor, required=True)

    meta = {
        'collection': 'Curso'
    }

    def __str__(self):
        return f"{self.nombre} - {self.idioma} ({self.nivel})"


class Inscripcion(Document):
    fecha_inscripcion = DateField(default=date.today)
    abono_propio = BooleanField(default=False)
    abono_inscripcion = DecimalField(precision=2, required=True)

    alumno = ReferenceField(Alumno, required=True)
    curso = ReferenceField(Curso, required=True)

    meta = {
        'collection': 'Inscripcion'
    }

    def __str__(self):
        return f"{self.alumno} → {self.curso}"

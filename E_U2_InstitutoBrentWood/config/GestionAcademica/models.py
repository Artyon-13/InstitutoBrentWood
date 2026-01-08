from django.db import models

class Alumno(models.Model):
    cedula = models.CharField(max_length=10,unique= True, primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    edad = models.IntegerField()

    class Meta:
        db_table = 'Alumno'

    def __str__(self):
        return f"{self.nombres} {self.apellidos} {self.cedula}"

class Profesor(models.Model):
    cedula = models.CharField(max_length=10, unique= True, primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=200)
    correo = models.EmailField(unique=True)

    class Meta:
        db_table = 'Profesor'

    def __str__(self):
        return f"{self.nombres} {self.apellidos} {self.cedula}"

class Curso(models.Model):
    nombre = models.CharField(max_length=20)
    idioma = models.CharField(max_length=20)
    nivel = models.CharField(max_length=20)

    profesor = models.OneToOneField(
        Profesor,
        on_delete=models.CASCADE,
        related_name='curso'
    )

    class Meta:
        db_table = 'Curso'

    def __str__(self):
        return self.nombre

class Inscripcion(models.Model):
    fecha_inscripcion = models.DateField()
    abono_propio = models.CharField(max_length=2)
    abono_inscripcion = models.DecimalField(max_digits=8, decimal_places=2)

    alumno = models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )

    curso = models.OneToOneField(
        Curso,
        on_delete=models.CASCADE,
        related_name='inscripcion'
    )

    class Meta:
        db_table = 'Inscripcion'

    def __str__(self):
        return f"{self.alumno.nombres} - {self.curso.nombre}"

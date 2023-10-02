# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError

class Univalluno(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    tipoUnivalluno = models.CharField(max_length=100)
    tipoDocumento = models.CharField(max_length=100)
    numeroDocumento = models.CharField(max_length=10)
    codigoEstudiante = models.CharField(max_length=10)
    correoElectrónico = models.CharField(max_length=100)

    def clean(self):
        if self.tipoUnivalluno == 'Estudiante':
            existing_univallunoCod = Univalluno.objects.exclude(id=self.id).filter(codigoEstudiante=self.codigoEstudiante)
            if existing_univallunoCod.exists():
                raise ValidationError('Ya existe un Univalluno con el mismo Código de estudiante registrado.')

    def clean(self):
        existing_univallunoTD = Univalluno.objects.exclude(id=self.id).filter(tipoDocumento=self.tipoDocumento)
        existing_univallunoID = Univalluno.objects.exclude(id=self.id).filter(numeroDocumento=self.numeroDocumento)
        if existing_univallunoID.exists() and existing_univallunoTD.exists():
            raise ValidationError('Ya existe un Univalluno con el mismo Tipo y Número de documento.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    

class ArticuloDeportivo(models.Model):
    nombre = models.CharField(max_length=100)
    deporte = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=100)

class Prestamo(models.Model):
    univalluno = models.ForeignKey(Univalluno, on_delete=models.CASCADE)
    articulo_deportivo = models.ForeignKey(ArticuloDeportivo, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()

    def __str__(self):
        return f"Prestamo de {self.univalluno.nombres} {self.univalluno.apellidos} - {self.articulo_deportivo.nombre}"


    



# Create your models here.
from django.db import models
from django.utils import timezone
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

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    

class ArticuloDeportivo(models.Model):
    nombre = models.CharField(max_length=100)
    deporte = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    valor = models.DecimalField(max_digits=10, decimal_places=3,default=0.0)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre}"

class Prestamo(models.Model):
    univalluno = models.ForeignKey(Univalluno, on_delete=models.CASCADE)
    articuloDeportivo = models.ForeignKey(ArticuloDeportivo, on_delete=models.CASCADE)
    fechaHoraPrestamo = models.DateTimeField(default=timezone.now)
    fechaHoraVencimiento = models.DateTimeField(default=timezone.now().replace(hour=20, minute=0, second=0, microsecond=0))

    def clean(self):
        # Verifica si el artículo deportivo está en préstamo
        if self.articuloDeportivo.prestamo_set.filter(fechaHoraVencimiento__isnull=False).exists():
            raise ValidationError('El artículo deportivo ya está en préstamo.')

    def save(self, *args, **kwargs):
        # Marcar el artículo deportivo como no disponible cuando se crea el préstamo
        if not self.id:
            self.articuloDeportivo.disponible = False
            self.articuloDeportivo.save()

        self.clean()
        super().save(*args, **kwargs)

    def completarPrestamo(self):
        # Marcar el artículo deportivo como disponible cuando se completa el préstamo
        self.articuloDeportivo.disponible = True
        self.articuloDeportivo.save()
    
    def __str__(self):
        return f"{self.univalluno}"

class Multas(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE, default=0)
    univalluno = models.ForeignKey(Univalluno, on_delete=models.CASCADE, default=0)
    valorMulta = models.PositiveIntegerField()
    estado = models.CharField(max_length=100)
    fechaMulta = models.DateTimeField(default=timezone.now)
    fechaPagoMulta = models.DateTimeField(null=True, blank=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.actualizarEstadoPrestamo()

    def actualizarEstadoPrestamo(self):
        # Verifica si la multa ha sido pagada y actualiza el estado del préstamo y disponibilidad del artículo
        if self.estado == 'Pagada':
            self.prestamo.completarPrestamo()
        else:
            self.prestamo.articuloDeportivo.disponible = False
            self.prestamo.articuloDeportivo.save()
    
    



from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from datetime import datetime, time
from .models import Multas, Prestamo
from .serializer import MultasSerializer

# Create your views here.

class MultasView(viewsets.ModelViewSet):
    serializer_class = MultasSerializer
    queryset = Multas.objects.all()
    

def generar_multas(request):
    # Obtén la hora actual
    ahora = datetime.now().time()
    # Obtén la fecha actual
    fecha_actual = datetime(2023, 1, 1, 20, 0)

    # Verifica si es posterior a las 8 PM (20:00)
    if ahora < time(20, 0):
        # Obtén los préstamos activos que están vencidos
        prestamos_vencidos = Prestamo.objects.filter(univalluno=1)
        contenedor=Prestamo.objects.values('fechaHoraVencimiento')
        # Genera una multa para cada préstamo vencido
        for prestamo in prestamos_vencidos:
            print(1)
            Multas.objects.create(
                univalluno=prestamo.univalluno,
                fechaMulta=datetime.now(),
                valorMulta=100,  # Establece el valor de la multa según tus requerimientos
                estado='Pendiente'  # Establece el estado inicial de la multa
            )
        
        print(prestamos_vencidos)

        return JsonResponse({"message": "Multas generadas exitosamente"})

    return JsonResponse({"message": "Aún no es hora de generar multas"})



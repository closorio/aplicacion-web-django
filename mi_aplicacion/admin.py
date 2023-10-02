from django.contrib import admin
from .models import Univalluno
from .models import ArticuloDeportivo
from .models import Prestamo



class UnivallunoAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        # Si se está creando un nuevo usuario, los campos son editables
        if not obj:
            return []
        # Si se está editando un usuario existente, los campos son solo de lectura
        else:
            return ['tipoDocumento', 'numeroDocumento']



class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('univalluno', 'articulo_deportivo', 'fecha_hora_prestamo', 'fecha_hora_vencimiento')





# Register your models here.

admin.site.register(Univalluno, UnivallunoAdmin)
admin.site.register(ArticuloDeportivo)
admin.site.register(Prestamo)

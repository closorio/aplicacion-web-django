from django.contrib import admin
from .models import Univalluno
from .models import ArticuloDeportivo
from .models import Prestamo


# Register your models here.

admin.site.register(Univalluno)
admin.site.register(ArticuloDeportivo)
admin.site.register(Prestamo)

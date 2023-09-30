from typing import Any, Dict
from django.contrib import admin
from django.forms import ModelForm
from .models import Univalluno
from .models import ArticuloDeportivo
from .models import Prestamo
from django.core.exceptions import ValidationError



# Register your models here.

class UnivallunoForm(ModelForm):

    def clean(self) -> Dict[str, Any]:
        print(self.cleaned_data)
        print(Univalluno.objects.all())
        
        print(self.instance.apellidos)
        # if len(self.instance.nombres) <= 4:
        #     raise ValidationError("holaaaa")
        
        return super().clean()
    class Meta:
        model = Univalluno
        fields = "__all__"


class UnivallunoAdmin(admin.ModelAdmin):
    form = UnivallunoForm


admin.site.register(Univalluno, UnivallunoAdmin)
admin.site.register(ArticuloDeportivo)
admin.site.register(Prestamo)

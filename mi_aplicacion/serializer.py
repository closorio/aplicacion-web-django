from rest_framework import serializers
from .models import Multas

class MultasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multas
        fields = '__all__'
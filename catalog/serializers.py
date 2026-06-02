from rest_framework import serializers
from .models import Ruta, Paquete

class PaqueteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paquete
        fields = ["id", "codigo_rastreo", "destinatario", "peso_kg", "tipo", "estado"]

class RutaSerializer(serializers.ModelSerializer):
    paquetes = PaqueteSerializer(many=True, read_only=True)

    class Meta:
        model = Ruta
        fields = ["id", "codigo", "paquetes"]

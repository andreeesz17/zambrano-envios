from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Ruta, Paquete
from .serializers import RutaSerializer, PaqueteSerializer

class RutaViewSet(viewsets.ModelViewSet):
    queryset = Ruta.objects.all().order_by("id")
    serializer_class = RutaSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["codigo"]
    ordering_fields = ["id", "codigo"]

class PaqueteViewSet(viewsets.ModelViewSet):
    queryset = Paquete.objects.select_related("codigo_rastreo").all().order_by("-id")
    serializer_class = PaqueteSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["codigo_rastreo", "estado", "tipo"]
    search_fields = ["destinatario", "codigo_rastreo__codigo"]
    ordering_fields = ["id", "destinatario", "peso_kg", "tipo", "estado"]

from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import RutaViewSet, PaqueteViewSet

router = DefaultRouter()
router.register(r"rutas", RutaViewSet, basename="rutas")
router.register(r"paquetes", PaqueteViewSet, basename="paquetes")

urlpatterns = []
urlpatterns += router.urls
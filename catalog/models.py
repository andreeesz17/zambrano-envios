from django.db import models

class Ruta(models.Model):
    codigo = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.codigo

class Paquete(models.Model):
    codigo_rastreo = models.ForeignKey(Ruta, on_delete=models.PROTECT, related_name="paquetes")
    destinatario = models.CharField(max_length=120)
    peso_kg = models.PositiveIntegerField()
    tipo = models.CharField(max_length=20)
    estado = models.CharField(max_length=60, blank=True, default="")

    def __str__(self):
        return f"{self.destinatario} - {self.codigo_rastreo.codigo}"


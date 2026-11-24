from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models


class Viaje(models.Model):
    titulo = models.CharField("Título del viaje", max_length=120)
    destino = models.CharField("Destino", max_length=120)
    pais = models.CharField("País", max_length=80)
    fecha_salida = models.DateField("Fecha de salida")
    duracion_dias = models.PositiveIntegerField(
        "Duración (días)",
        validators=[MinValueValidator(1)],
    )
    precio = models.DecimalField(
        "Precio",
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
    )
    cupos_disponibles = models.IntegerField(
        "Cupos disponibles",
        validators=[MinValueValidator(0)],
    )
    correo_contacto = models.EmailField("Correo de contacto", max_length=150)
    descripcion = models.TextField("Descripción", blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["fecha_salida", "titulo"]
        verbose_name = "Viaje"
        verbose_name_plural = "Viajes"

    def __str__(self):
        return f"{self.titulo} - {self.destino} ({self.pais})"
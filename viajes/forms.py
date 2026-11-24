from django import forms
from .models import Viaje


class ViajeForm(forms.ModelForm):
    class Meta:
        model = Viaje
        fields = [
            "titulo",
            "destino",
            "pais",
            "fecha_salida",
            "duracion_dias",
            "precio",
            "cupos_disponibles",
            "correo_contacto",
            "descripcion",
        ]
        widgets = {
            "fecha_salida": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "destino": forms.TextInput(attrs={"class": "form-control"}),
            "pais": forms.TextInput(attrs={"class": "form-control"}),
            "duracion_dias": forms.NumberInput(attrs={"class": "form-control"}),
            "precio": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "cupos_disponibles": forms.NumberInput(attrs={"class": "form-control"}),
            "correo_contacto": forms.EmailInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }
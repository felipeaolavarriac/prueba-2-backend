from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar_viajes, name="listar_viajes"),
    path("crear/", views.crear_viaje, name="crear_viaje"),
    path("editar/<int:pk>/", views.editar_viaje, name="editar_viaje"),
    path("eliminar/<int:pk>/", views.eliminar_viaje, name="eliminar_viaje"),
]
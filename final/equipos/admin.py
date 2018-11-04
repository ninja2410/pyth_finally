from django.contrib import admin
from equipos.models import Jugador, Equipo, JugadorAdmin, Partido, PartidoAdmin
# Register your models here.
admin.site.register(Jugador, Equipo)
admin.site.register(Partido, PartidoAdmin)

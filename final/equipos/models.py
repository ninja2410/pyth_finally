from django.db import models
from django.contrib import admin

# Create your models here.

class Jugador(models.Model):

    nombre  =   models.CharField(max_length=30)
    apellido  =   models.CharField(max_length=30)
    camisola  =   models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()

    def __str__(self):

        return self.nombre

class Equipo(models.Model):
    nombre    = models.CharField(max_length=60)
    departamento    = models.CharField(max_length=60)
    categoria    = models.CharField(max_length=60)
    anio      = models.IntegerField()
    actores   = models.ManyToManyField(Actor, through='Actuacion')

class Partido (models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

class PartidoInLine(admin.TabularInline):
    model = Partido
    extra = 1


class JugadorAdmin(admin.ModelAdmin):
    inlines = (PartidoInLine,)


class PartidoAdmin (admin.ModelAdmin):
    inlines = (PartidoInLine,)

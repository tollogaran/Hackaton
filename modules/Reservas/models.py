from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

TAGS = (
	('S', 'Pequeña'),
	('M', 'Mediana'),
	('G', 'Grande'),
	)

class Sala(models.Model):
	id = models.AutoField(primary_key=True)
	sala = models.CharField(max_length=50)
	horario_inicio = models.CharField(max_length=50)
	horario_termino = models.CharField(max_length=50)
	cantidad_usuarios = models.CharField(max_length=50)
	fecha_reserva = models.DateField(default=datetime.date.today)
	fecha_creacion = models.DateField(auto_now=True)
	autor = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return "%s %s" % ("Sala: ", self.sala)
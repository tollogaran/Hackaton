from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Sala
#from modules.Publicaciones.serializers import PublicacionSerializer

# para tablas que están relacionadas
# es la tercera clase del ejemplo, pero se mueve al principio
class SalaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sala
        fields = ('sala', 
        			'horario_inicio', 
        			'horario_termino', 
        			'cantidad_usuarios', 
        			'fecha_reserva',
        			'autor',
        			)
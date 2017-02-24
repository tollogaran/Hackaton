from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
#from .serializers import UserSerializer,UserSecondSerializer

# PARA LA SEGUNDA class UserDetail
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework import generics, filters

# Para clase de filtros
#from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework import filters



#Vistas basadas en clases
class SalaList(generics.ListCreateAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer


# Clase genérica que hace lo mismo que Userdetail get, put y delete (RetrieveUpdateDestroy)
class SalasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

from django.shortcuts import render
from rest_framework import generics
from .serializers import SedesSerializer, HorariosSerializer, PlanesSerializer, CategoriasSerializer, RutinasSerializer
from .models import Sedes, Horarios, Planes, Categorias, Rutinas

# Create your views here.

class SedesListCreate(generics.ListCreateAPIView):
    queryset = Sedes.objects.all()
    serializer_class = SedesSerializer

class SedesUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sedes.objects.all()
    serializer_class = SedesSerializer

class HorariosListCreate(generics.ListCreateAPIView):
    queryset = Horarios.objects.all()
    serializer_class = HorariosSerializer

class HorariosUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Horarios.objects.all()
    serializer_class = HorariosSerializer

class PlanesListCreate(generics.ListCreateAPIView):
    queryset = Planes.objects.all()
    serializer_class = PlanesSerializer

class PlanesUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Planes.objects.all()
    serializer_class = PlanesSerializer

class PlanesListCreate(generics.ListCreateAPIView):
    queryset = Planes.objects.all()
    serializer_class = PlanesSerializer

class CategoriasUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer

class CategoriasListCreate(generics.ListCreateAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer

class RutinasUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rutinas.objects.all()
    serializer_class = RutinasSerializer

class RutinasListCreate(generics.ListCreateAPIView):
    queryset = Rutinas.objects.all()
    serializer_class = RutinasSerializer
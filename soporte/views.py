from django.shortcuts import render
from rest_framework import generics

from soporte.models import Sede
from .serializers import PQRSerializer, PersonaSoporteSerializer, SedeSerializer
from .serializers import PersonaSoporte
from .serializers import PQR, Sede
# Create your views here.

class PersonaSoporteListCreate(generics.ListCreateAPIView):
    queryset = PersonaSoporte.objects.all()
    serializer_class = PersonaSoporteSerializer

class PersonaSoporteUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonaSoporte.objects.all()
    serializer_class = PersonaSoporteSerializer

class PQRListCreate(generics.ListCreateAPIView):
    queryset = PQR.objects.all()
    serializer_class = PQRSerializer

class PQRUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = PQR.objects.all()
    serializer_class = PQRSerializer

class SedeListCreate(generics.ListCreateAPIView):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer

class SedeUpdatedDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer
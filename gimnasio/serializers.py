from rest_framework import serializers
from .models import Sedes, Horarios, Planes, Categorias, Rutinas

class SedesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sedes
        fields = ['nombre', 'direccion', 'telefono']

class HorariosSerializer(serializers.ModelSerializer):
    sedes = SedesSerializer(read_only=True)

    class Meta:
        model = Horarios
        fields = ['sedes','dia', 'hora_inicio', 'hora_fin']

class PlanesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planes
        fields = ['nombre', 'tiempo', 'valor']

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sedes
        fields = ['nombre']

class RutinasSerializer(serializers.ModelSerializer):
    categorias = CategoriasSerializer(read_only=True)

    class Meta:
        model = Rutinas
        fields = ['categorias','descripcion']

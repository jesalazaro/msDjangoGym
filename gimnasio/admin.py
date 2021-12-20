from django.contrib import admin
from .models import Horarios, Sedes, Planes, Categorias, Rutinas

# Register your models here.

admin.site.register(Horarios)
admin.site.register(Sedes)
admin.site.register(Planes)
admin.site.register(Categorias)
admin.site.register(Rutinas)
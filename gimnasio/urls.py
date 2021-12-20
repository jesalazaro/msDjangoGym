from django.urls import path
from .views import SedesListCreate, SedesUpdateDelete, HorariosListCreate, HorariosUpdateDelete, PlanesListCreate, PlanesUpdateDelete, CategoriasListCreate, CategoriasUpdateDelete, RutinasListCreate, RutinasUpdateDelete


urlpatterns = [
    path('sedes/', SedesListCreate.as_view()),
    path('sedes/<pk>/', SedesUpdateDelete.as_view()),
    path('horarios/', HorariosListCreate.as_view()),
    path('horarios/<pk>/', HorariosUpdateDelete.as_view()),
    path('planes/', PlanesListCreate.as_view()),
    path('planes/<pk>/', PlanesUpdateDelete.as_view()),
    path('categorias/', CategoriasListCreate.as_view()),
    path('categorias/<pk>/', CategoriasUpdateDelete.as_view()),
    path('rutinas/', RutinasListCreate.as_view()),
    path('rutinas/<pk>/', RutinasUpdateDelete.as_view())
    ]
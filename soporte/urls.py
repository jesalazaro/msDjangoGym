from django.urls import path
from django.urls.resolvers import URLPattern
from .views import PersonaSoporteListCreate, PersonaSoporteUpdateDelete, PQRListCreate, PQRUpdateDelete, SedeListCreate, SedeUpdatedDelete

urlpatterns = [
    path('personas-soporte/', PersonaSoporteListCreate.as_view()),
    path('personas-soporte/<pk>/', PersonaSoporteUpdateDelete.as_view()),
    path('pqr/', PQRListCreate.as_view()),
    path('pqr/<pk>', PQRUpdateDelete.as_view()),
    path('sede/', SedeListCreate.as_view()),
    path('sede/<pk>', SedeUpdatedDelete.as_view())
]
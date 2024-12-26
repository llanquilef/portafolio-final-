from django.shortcuts import render
from rest_framework import viewsets
from .models import RecomendacionPersonal, RecomendacionUsuario
from .serializers import RecomendacionPersonalSerializer, RecomendacionUsuarioSerializer, UsuarioSerializer
from django.contrib.auth.models import User


# Index

def Index(request):
    
    """ Vista para ver el Index """
    
    return render(request, 'index.html')    
    
    
# Usuarios
 
class UserViewSet(viewsets.ModelViewSet):
    """
    Vista que permite apuntar al registro de mis rutas de la API para visualizar mis recomendaciones personales.
    
    """
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
     
# Recomendación Personal

class R_PersonalViewSet(viewsets.ModelViewSet):
    """
    Vista que permite apuntar al registro de mis rutas de la API para visualizar mis recomendaciones personales.
    
    """
    queryset = RecomendacionPersonal.objects.all()
    serializer_class = RecomendacionPersonalSerializer
     
     
     
# Recomendación Usuario

class R_UsuarioViewSet(viewsets.ModelViewSet):
    """
    Vista que permite apuntar al registro de mis rutas de la API para visualizar las recomendaciones de los usuarios de la página.
    
    """
    queryset = RecomendacionUsuario.objects.all()
    serializer_class = RecomendacionUsuarioSerializer
     
from django.contrib import admin
from .models import RecomendacionPersonal, RecomendacionUsuario

admin.site.register(RecomendacionUsuario)
admin.site.register(RecomendacionPersonal)

# Register your models here.

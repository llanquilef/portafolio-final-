from tkinter import TRUE
from django.db import models


class RecomendacionPersonal(models.Model):
    nombre = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    comentario = models.TextField(max_length=600)
    añoPublicacion = models.DateField()
    TIPO_MULTIMEDIA = [
        ('Película', 'Película'),
        ('Libro', 'Libro'),
        ('Serie', 'Serie'),
        ('Albúm', 'Albúm'),
        ('Podcast', 'Podcast'),
        ('Cómic', 'Cómic'),
        ('Anime', 'Anime'),
        ('Manga', 'Manga'),
    ]
    tipoMultimedia = models.CharField(max_length=50, choices=TIPO_MULTIMEDIA)
    fechaPost = models.DateField(auto_now_add=TRUE)
    horaPost = models.DateField(auto_now_add=TRUE)
    
class RecomendacionUsuario(models.Model):
    nombre = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    comentario = models.TextField(max_length=600)
    añoPublicacion = models.DateField()
    TIPO_MULTIMEDIA = [
        ('Película', 'Película'),
        ('Libro', 'Libro'),
        ('Serie', 'Serie'),
        ('Albúm', 'Albúm'),
        ('Podcast', 'Podcast'),
        ('Cómic', 'Cómic'),
        ('Anime', 'Anime'),
        ('Manga', 'Manga'),
    ]
    tipoMultimedia = models.CharField(max_length=50, choices=TIPO_MULTIMEDIA)
    fechaPost = models.DateField(auto_now_add=TRUE)
    horaPost = models.DateField(auto_now_add=TRUE)
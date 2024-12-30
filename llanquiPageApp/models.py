from django.db import models

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


class RecomendacionPersonal(models.Model):
    nombre = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    comentario = models.TextField(max_length=600)
    añoPublicacion = models.DateField()
    tipoMultimedia = models.CharField(max_length=50, choices=TIPO_MULTIMEDIA)
    fechaPost = models.DateField(auto_now_add=True)
    horaPost = models.TimeField(auto_now_add=True)
    
class RecomendacionUsuario(models.Model):
    nombre = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    comentario = models.TextField(max_length=600)
    añoPublicacion = models.DateField()

    tipoMultimedia = models.CharField(max_length=50, choices=TIPO_MULTIMEDIA)
    fechaPost = models.DateField(auto_now_add=True)
    horaPost = models.TimeField(auto_now_add=True)
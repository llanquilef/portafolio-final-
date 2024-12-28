# Generated by Django 5.1.3 on 2024-12-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecomendacionPersonal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('autor', models.CharField(max_length=150)),
                ('comentario', models.TextField(max_length=600)),
                ('añoPublicacion', models.DateField()),
                ('tipoMultimedia', models.CharField(choices=[('Película', 'Película'), ('Libro', 'Libro'), ('Serie', 'Serie'), ('Albúm', 'Albúm'), ('Podcast', 'Podcast'), ('Cómic', 'Cómic'), ('Anime', 'Anime'), ('Manga', 'Manga')], max_length=50)),
                ('fechaPost', models.DateField(auto_now_add=True)),
                ('horaPost', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecomendacionUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('autor', models.CharField(max_length=150)),
                ('comentario', models.TextField(max_length=600)),
                ('añoPublicacion', models.DateField()),
                ('tipoMultimedia', models.CharField(choices=[('Película', 'Película'), ('Libro', 'Libro'), ('Serie', 'Serie'), ('Albúm', 'Albúm'), ('Podcast', 'Podcast'), ('Cómic', 'Cómic'), ('Anime', 'Anime'), ('Manga', 'Manga')], max_length=50)),
                ('fechaPost', models.DateField(auto_now_add=True)),
                ('horaPost', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]

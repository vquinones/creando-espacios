# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField


class UEPTemplate(models.Model):
    title = models.CharField('Titulo Principal', max_length=50, default="")
    detail = models.CharField('Detalle de la página Principal', max_length=500, default="")
    body = RichTextField('Texto completo', default="")

    title_articles = models.CharField('Articulos, intro ...', max_length=700, default="")
    title_events = models.CharField('Eventos, intro ...', max_length=700, default="")
    title_galleries = models.CharField('Galerías, intro ...', max_length=700, default="")
    title_teachers = models.CharField('Docentes, intro ...', max_length=700, default="")

    photo_1 = models.ImageField('Primera foto de portada', upload_to='profiles', max_length=200, null=True, blank=True)
    title_photo_1 = models.CharField('Titulo o Frase', max_length=50, default="")
    detail_photo_1 = models.CharField('Detalle', max_length=500, default="")

    photo_2 = models.ImageField('Segunda foto de portada', upload_to='profiles', max_length=200, null=True, blank=True)
    title_photo_2 = models.CharField('Titulo o Frase', max_length=50, default="")
    detail_photo_2 = models.CharField('Detalle', max_length=500, default="")

    photo_3 = models.ImageField('Tercera foto de portada', upload_to='profiles', max_length=200, null=True, blank=True)
    title_photo_3 = models.CharField('Titulo o Frase', max_length=50, default="")
    detail_photo_3 = models.CharField('Detalle', max_length=500, default="")

    photo_4 = models.ImageField('Cuarta foto de portada', upload_to='profiles', max_length=200, null=True, blank=True)
    title_photo_4 = models.CharField('Titulo o Frase', max_length=50, default="")
    detail_photo_4 = models.CharField('Detalle', max_length=500, default="")

    def __unicode__(self):
        return self.title


class Docentes(models.Model):
    name = models.CharField('Apellido y Nombre', max_length=60, default="", null=False, blank=False)
    detail = models.TextField('Resumen del Docente', max_length=500, default="")
    photo = models.ImageField('Foto de Perfil', upload_to='profiles', max_length=200, null=True, blank=True)
    publico = models.BooleanField('Publicar?', default=False)

    def __str__(self):
        return self.name


class Eventos(models.Model):
    title = models.CharField('Título del Evento', max_length=60, default="", null=False, blank=False)
    lugar = models.CharField('Lugar', max_length=100, default="", null=False, blank=False)
    detail = RichTextField('Detalle del evento', max_length=500, default="")
    start_date = models.DateTimeField('Fecha del evento')
    publico = models.BooleanField('Publicar?', default=False)

    def __unicode__(self):
        return self.title


class Galeria(models.Model):
    title = models.CharField('Nombre de la Galería', max_length=60, default="", null=False, blank=False)
    detail = models.TextField('Detalle', max_length=500, default="")
    photo = models.ImageField('Foto de portada', upload_to='photos', max_length=200, null=True, blank=True)
    publico = models.BooleanField('Publicar?', default=False)

    def __unicode__(self):
        return self.title


class GaleriaPhotos(models.Model):
    galeria = models.ForeignKey(Galeria, related_name='photos')
    photo = models.ImageField('Foto', upload_to='photos', max_length=200, null=True, blank=True)
    detail = RichTextField('Detalle de la foto', max_length=500, default="")

    def __unicode__(self):
        return self.photo.url


class Articulos(models.Model):
    title = models.CharField('Título del Artículo', max_length=60, default="", null=False, blank=False)
    autor = models.CharField('Autor', max_length=60, default="", null=False, blank=False)
    email = models.CharField('Corre Electrónico', max_length=80, default="", null=True, blank=True)
    detail = RichTextField('Detalle del Artículo', max_length=500, default="")
    file = models.FileField('Archivo PDF', upload_to='articles', max_length=200, null=True, blank=True)
    date = models.DateTimeField('Fecha de Publicación')
    publico = models.BooleanField('Publicar?', default=False)

    def __unicode__(self):
        return self.title


class Mensajes(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    nombre_completo = models.CharField(max_length=100, default="", null=False, blank=False)
    email = models.CharField(max_length=100, default="", null=False, blank=False)
    titulo = models.CharField(max_length=100, default="", null=False, blank=False)
    mensaje = models.CharField(max_length=2000, default="", null=False, blank=False)
    estado = models.BooleanField()

    def __unicode__(self):
        return self.nombre_completo

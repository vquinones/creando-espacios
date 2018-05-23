# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *


class GaleriaPhotosInline(admin.StackedInline):
    model = GaleriaPhotos
    extra = 1


class GaleriaAdmin(admin.ModelAdmin):
    inlines = [GaleriaPhotosInline, ]


admin.site.register(UEPTemplate)
admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(Docentes)
admin.site.register(Eventos)
admin.site.register(Articulos)
admin.site.register(Mensajes)

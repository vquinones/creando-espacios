# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date
from django.views.generic import TemplateView
from uep191.settings import MEDIA_URL
from .models import *
from django.views.decorators.cache import cache_page


class HomeView(TemplateView):
    template_name = "index.html"

    def post(self, request, *args, **kwargs):
        try:
            messages = Mensajes()
            messages.nombre_completo = request.POST.get('name')
            messages.email = request.POST.get('email')
            messages.titulo = request.POST.get('subject')
            messages.mensaje = request.POST.get('message')
            messages.estado = False
            messages.save()
        except:
            pass

        return self.get(request)

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(**kwargs)
        uep_data = UEPTemplate.objects.all()
        events = Eventos.objects.all()
        gallery = Galeria.objects.all()[:1]
        teachers = Docentes.objects.all()
        request.session['ARTICLE_TEXT'] = uep_data[0].title_articles
        request.session['GALLERY_TEXT'] = uep_data[0].title_galleries
        request.session['TEACHER_TEXT'] = uep_data[0].title_teachers
        request.session['EVENT_TEXT'] = uep_data[0].title_events
        data = {
            'media': MEDIA_URL,
            'title': uep_data[0].title,
            'detail': uep_data[0].detail,
            'body': uep_data[0].body,
            'events': events,
            'gallery': gallery,
            'teachers': teachers,
            'uep': uep_data[0],
            'photo_1': uep_data[0].photo_1,
            'photo_1_title': uep_data[0].title_photo_1,
            'photo_1_detail': uep_data[0].detail_photo_1,
        }
        context.update(data)
        return self.render_to_response(context)


class GalleryView(TemplateView):
    template_name = 'gallery.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        gallery_id = kwargs['gallery_id']
        gallery = None
        photos = None
        galleries = None

        try:
            if gallery_id is not None:
                gallery = Galeria.objects.get(id=gallery_id)
                photos = gallery.photos.all()
        except:
            all_galleries = Galeria.objects.filter(publico=True)
            galleries = all_galleries

        data = {
            'media': MEDIA_URL,
            'galleries': galleries,
            'gallery': gallery,
            'photos': photos,
            'gallery_title': request.session['GALLERY_TEXT']
        }
        context.update(data)
        return self.render_to_response(context)


class DocentesView(TemplateView):
    template_name = 'teacher.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        teachers = Docentes.objects.filter(publico=True)

        data = {
            'media': MEDIA_URL,
            'teachers': teachers,
            'teacher_title': request.session['TEACHER_TEXT']
        }
        context.update(data)
        return self.render_to_response(context)


class ArticulosView(TemplateView):
    template_name = 'article.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        articles = Articulos.objects.filter(publico=True).order_by('-date')

        data = {
            'media': MEDIA_URL,
            'articles': articles,
            'article_title': request.session['ARTICLE_TEXT']
        }
        context.update(data)
        return self.render_to_response(context)


class EventosView(TemplateView):
    template_name = 'events.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        yesterday = date.today()
        events = Eventos.objects.filter(start_date__gte=yesterday, publico=True).order_by('-start_date')

        data = {
            'media': MEDIA_URL,
            'events': events,
            'event_title': request.session['EVENT_TEXT']
        }
        context.update(data)
        return self.render_to_response(context)

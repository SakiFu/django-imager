from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from imager_images.models import Photo


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        photo = Photo.objects.all().filter(published='public').order_by('?').first()
        context['photo'] = photo
        return context
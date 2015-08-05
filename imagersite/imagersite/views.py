from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from imager_images.models import Photo, Album


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        photo = Photo.objects.all().filter(published='public').order_by('?').first()
        context['photo'] = photo
        return context

class AlbumAddView(CreateView):
    template_name = 'album_add.html'
    model = Album
    fields = ['title', 'description', 'published', 'photos']
    success_url = '/images/library/'

    def get_form(self):
        form = super(AlbumAddView, self).get_form()
        form.fields['photos'].queryset = Photo.objects.filter(
            user=self.request.user
        )
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(AlbumAddView, self).form_valid(form)
from django.shortcuts import render
from .models import Photo
from .models import Album
from django.views.generic import TemplateView, DetailView
from django.db.models import Q
# from settings import MEDIA_URL, STATIC_URL
# Create your views here.

class IndexView(TemplateView):
    template = 'index.html'

    def get_context_data(self, **kwargs):
        photos = Photo.objects.filter(published='public').order_by('?').first()
        context = super(IndexView, self).get_context_data(**kwargs)
        context['photo'] = photo
        return context


class PhotoView(DetailView):
    model = Photo
    template_name = 'photo.html'
    detect = False

    def get_queryset(self, *args, **kwargs):
        return super(PhotoView, self).get_queryset(*args, **kwargs).filter(
            Q(user=self.request.user) | Q(published='Public'))

    # def get_context_data(self, **kwargs):
    #     context = super(DetailView, self).get_context_data(**kwargs)
    #     if self.detect and len(self.object.faces.all()) == 0:
    #         get_faces(self.object)

    #     context['faces'] = self.object.faces.all()
    #     return context


class AlbumView(DetailView):
    model = Album
    template_name = 'album.html'

    def get_queryset(self, *args, **kwargs):
        return super(AlbumView, self).get_queryset(*args, **kwargs).filter(
            Q(user=self.request.user) | Q(published='Public'))

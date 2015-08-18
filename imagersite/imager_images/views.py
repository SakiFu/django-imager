from django.shortcuts import render
from .models import Photo, Album, FaceRecognition
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView
from django.db.models import Q
from django.forms.models import ModelForm
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.views import redirect_to_login
from django.http import Http404
import os
# from settings import MEDIA_URL, STATIC_URL
# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_faces(photo):
    import Algorithmia
    import base64
    Algorithmia.apiKey = os.environ['Simple simkBOjTtJ05lfuY+E03zcdDKm61']
    file_path = 'media/' + str(photo.file)
    file_path = os.path.join(BASE_DIR, file_path)

    with open(file_path, 'rb') as img:
        b64 = base64.b64encode(img.read())

    result = Algorithmia.algo("/ANaimi/FaceDetection").pipe(b64)

    faces = []
    for rect in result:
        face = FaceRecognition()
        face.photo = photo
        face.name = '?'
        face.x = rect['x']
        face.y = rect['y']
        face.width = rect['width']
        face.height = rect['height']
        face.save()
        faces.append(face)
    return faces

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


class PhotoAddView(CreateView):
    template_name = 'photo_add.html'
    model = Photo
    fields = ['image', 'title', 'description', 'published']
    success_url = '/images/library/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(PhotoAddView, self).form_valid(form)


class PhotoEditView(UpdateView):
    template_name = 'photo_edit.html'
    model = Photo
    fields = ['image', 'title', 'description', 'published']
    success_url = '/images/library/'

    def get_object(self):
        try:
            obj = Photo.objects.get(user=self.request.user,
                                    pk=self.kwargs['pk'])
        except Photo.DoesNotExist:
            raise Http404
        return obj

    def form_valid(self, form):
        form.save()
        return super(PhotoEditView, self).form_valid(form)


class AlbumView(DetailView):
    model = Album
    template_name = 'album.html'

    def get_queryset(self, *args, **kwargs):
        return super(AlbumView, self).get_queryset(*args, **kwargs).filter(
            Q(user=self.request.user) | Q(published='Public'))


class AlbumAddView(CreateView):
    template_name = 'album_add.html'
    model = Album
    fields = ['title', 'description', 'published']
    success_url = '/images/library/'

    def get_form(self):
        form = super(AlbumAddView, self).get_form()
        # form.fields['photos'].queryset = Photo.objects.filter(
        #     user=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(AlbumAddView, self).form_valid(form)


class AlbumEditView(UpdateView):
    template_name = 'album_edit.html'
    model = Album
    fields = ['title', 'description', 'published', 'photos', 'cover']
    success_url = '/images/library/'

    def get_object(self):
        try:
            obj = Album.objects.get(user=self.request.user,
                                    pk=self.kwargs['pk'])
        except Album.DoesNotExist:
            raise Http404
        return obj

    def get_form(self):
        form = super(AlbumEditView, self).get_form()
        form.fields['photos'].queryset = Photo.objects.filter(
            user=self.request.user)
        form.fields['cover'].queryset = form.instance.photos
        return form

    def form_valid(self, form):
        form.save()
        return super(AlbumEditView, self).form_valid(form)
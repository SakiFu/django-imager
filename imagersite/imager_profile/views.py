from django.shortcuts import render
from .models import Photos
from django.views.generic import TemplateView, ListView, DetailView
from imager_images.models import Photos, Album

# Create your views here.
class LibraryView(ListView):
    template_name = 'library.html'
    model = Photos
    
    def get_queryset(self):
        photos = None
        try:
            photos = Photos.objects.filter(
                                           published='public',
                                           user=self.request.user)
        except TypeError:
            pass
        
        return photos


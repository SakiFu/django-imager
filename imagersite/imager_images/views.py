from django.shortcuts import render
from .models import Photo
from django.views.generic import TemplateView
# from settings import MEDIA_URL, STATIC_URL
# Create your views here.

class IndexView(TemplateView):
    template = 'index.html'

    def get_context_data(self, **kwargs):
        photo = Photo.objects.filter(published='public').order_by('?').first()
        context = super(IndexView, self).get_context_data(**kwargs)
        context['photo'] = photo
        return context


# @login_required
# def library_view(request, *args, **kwargs):
#     return render(request, 'library.html', {})


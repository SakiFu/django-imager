from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from imager_images.models import Photo, Album

# Create your views here.
# class LibraryView(ListView):
#     template_name = 'library.html'
#     model = Photos
    
#     def get_queryset(self):
#         photos = None
#         try:
#             photos = Photos.objects.filter(
#                                            published='public',
#                                            user=self.request.user)
#         except TypeError:
#             pass
        
#         return photos

# class LibraryView(TemplateView):
#     template = 'library.html
#     def get_context_data(self, **kwargs):
#         photos = Photo.objects.filter(published='public').order_by('?').first()
#         context = super(LibraryView, self).get_context_data(**kwargs)
#         context['photo'] = photo
#         return context

# @login_required
# def library_view(request, *args, **kwargs):
#     return render(request, 'library.html', {})
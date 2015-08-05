from django.shortcuts import render
from django.views.generic import UpdateView
from imager_profile.models import ImagerProfile
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect


class ImagerProfileUpdateView(UpdateView):
    def dispatch(self, request, *args, **kwargs):
        profile = ImagerProfile.objects.get(id=int(self.kwargs['pk']))
        user_profile = ImagerProfile.objects.get(user=self.request.user)
        if profile != user_profile:
            return redirect('/accounts/login/')
        return super(ImagerProfileUpdateView, self).dispatch(request, *args, **kwargs)

    model = ImagerProfile
    template_name = 'profile_edit.html'
    fields = (
        'camera',
        'address',
        'website_url',
        'photography_type'
        )
    # success_url = reverse_lazy('profile')

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
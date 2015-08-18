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
    success_url = reverse_lazy('profile')

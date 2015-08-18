from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from imager_profile.views import ImagerProfileUpdateView

urlpatterns = [
    url(r'^$',
        login_required(TemplateView.as_view(template_name='profile.html')),
        name='profile'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(ImagerProfileUpdateView.as_view()), name='profile_edit')

]
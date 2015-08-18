from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
import views

urlpatterns = [
    url(r'^library/', login_required(TemplateView.as_view(template_name='library.html'))),
]
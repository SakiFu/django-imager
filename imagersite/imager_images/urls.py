from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from imager_images.views import  PhotoView, AlbumView
import views

urlpatterns = [
    # url(r'^home/$', views.IndexView.as_view(), name='index'),
    url(r'^library/', login_required(TemplateView.as_view(template_name='library.html'))),
    # url(r'^album/(?P<pk>\d+)/$',
    #     login_required(AlbumView.as_view()),
    #     name='album'),
    # url(r'^photos/(?P<pk>\d+)/$',
    #     login_required(PhotoView.as_view()),
    #     name='photo'),
]

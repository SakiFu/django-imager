"""imagersite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
import views
from imager_images.views import  PhotoView, AlbumView


urlpatterns = [
#    url(r'^imager/', include('imager_images.urls')),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^profile/', include('imager_profile.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^images/', include('imager_images.urls')),
        url(r'^images/album/(?P<pk>\d+)/$',
        login_required(AlbumView.as_view()),
        name='album'),
    url(r'^images/photos/(?P<pk>\d+)/$',
        login_required(PhotoView.as_view()),
        name='photo'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
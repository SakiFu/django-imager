from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^home/$', views.IndexView.as_view(), name='index'),
]

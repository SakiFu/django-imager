from rest_framework import viewsets
from imager_images.models import Photo
from django.db.models import Q
from serializers import PhotoSerializer
# Create your views here.


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get_queryset(self):
        qs = super(PhotoViewSet, self).get_queryset()
        is_mine = Q(user=self.request.user)
        is_public = Q(published='Public')
        if self.request.user.is_anonymous():
            qs = qs.filter(is_public)
        else:
            qs = qs.filter((is_public | is_mine)).distinct()
        return qs

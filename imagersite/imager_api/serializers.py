from imager_images.models import Photo
from rest_framework import serializers


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ('title',
                  'description',
                  'date_created',
                  'date_modified',
                  'date_published',
                  'published')
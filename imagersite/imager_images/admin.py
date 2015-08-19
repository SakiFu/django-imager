from django.contrib import admin
from .models import Photo
from .models import Album, Face
# Register your models here.

admin.site.register(Photo)
admin.site.register(Album)
admin.site.register(Face)

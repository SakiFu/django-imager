# from django.contrib import admin
from .models import ImagerProfile
from django.contrib.gis import admin
from django.core.urlresolvers import reverse

admin.site.register(ImagerProfile)

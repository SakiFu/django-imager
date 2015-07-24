from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    file = models.ImageField(upload_to='/photo_files/%Y-%m-%d')


class Album(models.Model):
    user = models.ForeignKey(User, related_name='albums', null=False)
    photos = models.ManyToManyField(
        Photos,
        related_name='albums',
        limit_choices_to=user)
    title = models.CharField(max_length=128)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now=True)
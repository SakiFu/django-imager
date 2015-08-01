from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

PUBLISHED_CHOICES = (
    ('private', 'private'),
    ('shared', 'shared'),
    ('public', 'public')
)


@python_2_unicode_compatible
class Photo(models.Model):
    image = models.ImageField(upload_to='photo_files/%Y-%m-%d')
    user = models.ForeignKey(
        User,
        null=False
    )
    title = models.CharField(max_length=128)
    description = models.TextField(help_text="Describe your photo.")
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now=True)
    published = models.CharField(max_length=256,
                                 choices=PUBLISHED_CHOICES,
                                 default='private')
    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Album(models.Model):
    user = models.ForeignKey(User, null=False)
    photos = models.ManyToManyField(
        Photo,
        related_name='albums',
        blank=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(null=True, blank=True)
    published = models.CharField(max_length=256,
                                 choices=PUBLISHED_CHOICES,
                                 default='private')
    cover = models.ForeignKey(Photo, related_name='cover_for')

    def __str__(self):
        return self.title

    @property
    def cover(self):
        qs = self.photos
        if qs.filter(is_cover=True).exists():
            qs = qs.filter(is_cover=True)
        return qs.order_by('?').first()


@python_2_unicode_compatible
class PhotoInAlbum(models.Model):
    photo = models.ForeignKey(Photo)
    album = models.ForeignKey(Album)
    is_cover = models.BooleanField(default=False)

    def __str__(self):
        return "{}: in album {}".format(self.photo, self.album)
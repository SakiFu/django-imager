from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

# Create your models here.


class ActiveProfileManager(models.Manager):
    """A model manger limited only to active profiles"""
    def get_queryset(self):
        """Filter the default queryset for active users"""
        query = super(ActiveProfileManager, self).get_queryset()
        return query.filter(user__is_active=True)


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    PHOTOGRAPHY_TYPE_CHOICES = (
        ('AB', 'Abstract'),
        ('AN', 'Animal'),
        ('AR', 'Artistic'),
        ('BE', 'Beauty'),
        ('FA', 'Fashion'),
        ('LA', 'Landscape'),
        ('NA', 'Nature'),
        ('PE', 'People'),
        ('TR', 'Travel'),
        ('WE', 'Wedding'),
    )
    user = models.OneToOneField(
        User,
        related_name='profile',
        null=False
    )

    camera = models.CharField(max_length=128,
                              help_text='What is model of your camera?')
    address = models.TextField()
    website_url = models.URLField()
    photography_type = models.CharField(
        max_length=64,
        help_text="What type of photography do you primarily take?",
        choices=PHOTOGRAPHY_TYPE_CHOICES
    )
    objects = models.Manager()
    active = ActiveProfileManager()

    def __str__(self):
        return self.user.get_full_name() or self.user.username

    def is_active(self):
        return self.user.is_active

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

class ActiveProfileManager(models.Manager):
    def get_queryset(self):
        query = super(ActiveProfileManager, self).get_queryset()
        return query.filter(is_active__exact=True)


@python_2_unicode_compatible
class ImagerProfile(models, Model):
    user = models.OneToOneField(
        user,
        related_name='+',
        null=False
        )

    camera = models.Charfield(max_length=128, help_text='What is model of your camera?')
    address = models.Textfield()
    website_url = models.UrlField()
    photography_type = models.CharField(
        max_length=64,
        helo_text="What type of photography do you primaliry make?",
        choices=PHOTOGRAPHY_TYPE_CHOICES
    )
    friends = models.ManyToManyField(User, related_name='friends')
    objects = models.Manager()
    active = ActiveProfileManager()

    def __str__(self):
        return self.user.get_full_name() or self.user.username

    def is_active(self):
        return self.user.is_active



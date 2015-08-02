from __future__ import unicode_literals
from django.test import TestCase
import factory
from faker import Factory
from . import models
from .models import Photo, Album
from django.contrib.auth.models import User

fake = Factory.create()


class UserFactory(factory.Factory):
    class Meta:
        model = User
    first_name = fake.first_name()
    email = factory.LazyAttribute(lambda n: "{}@example.com".format(
        n.username))
    username = factory.Sequence(lambda n: "user{}".format(n))


class PhotoFactory(factory.Factory):
    class Meta:
        model = Photo


class AlbumFactory(factory.Factory):
    class Meta:
        model = Album


class PhotoTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.user.save()
        self.photo = PhotoFactory.create(user=self.user)

    def tearDown(self):
        User.objects.all().delete()
        Photo.objects.all().delete()

    def test_add_photo(self):
        self.assertTrue(Photo.objects.count() == 0)
        self.photo.save()
        self.assertTrue(Photo.objects.count() == 1)

    def test_photo_user(self):
        self.assertTrue(self.photo.user)
        self.assertNotEqual(self.photo.user, UserFactory.create())


class AlbumTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.user.save()
        self.cover = PhotoFactory.create(user=self.user)
        self.cover.save()
        self.album = AlbumFactory(user=self.user)

    def test_add_album(self):
        self.assertTrue(Album.objects.count() == 0)
        self.album.save()
        self.assertTrue(Album.objects.count() == 1)

    def test_album_belonger(self):
        self.album.save()
        self.assertTrue(self.album.user)
        self.assertFalse(self.album.user is UserFactory.create())

    def test_add_photos_to_albums(self):
        self.album.save()
        self.assertTrue(self.album.photos.count() == 0)
        photo = PhotoFactory.create(user=self.user)
        photo.save()
        self.album.photos.add(photo)
        self.assertTrue(self.album.photos.count() == 1)

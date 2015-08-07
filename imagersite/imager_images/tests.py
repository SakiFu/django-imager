from __future__ import unicode_literals
from django.test import TestCase
import factory
from faker import Factory
from . import models
from .models import Photo, Album
from django.contrib.auth.models import User
from django.test import Client

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
    title = 'title_test_album'
    description = 'description_test_photo'


class AlbumFactory(factory.Factory):
    class Meta:
        model = Album
    title = 'title_test_album'
    description = 'description_album_test'


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

    def test_add_albums(self):
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


class AlbumViewTestCase(TestCase):

    def setUp(self):
        user = UserFactory.create(username='user1')
        user.set_password('user1_password')
        user.save()
        user2 = UserFactory.create(username='user2')
        user2.set_password('user2_password')
        user2.save()
        cover = PhotoFactory.create(user=user)
        cover.save()
        album = AlbumFactory.create(cover=cover, user=user)
        album.save()
        album.photos.add(cover)

    def test_album_view(self):
        album = Album.objects.all()[0]
        photo = Photo.objects.all()[0]
        c = Client()
        c.login(username='user1', password='user1_password')
        response = c.get('/images/album/{}/'.format(album.id))
        self.assertIn(album.title, response.content)
        self.assertIn(album.description, response.content)
        self.assertIn(photo.title, response.content)

    def test_album_nonuser(self):
        album = Album.objects.all()[0]
        c = Client()
        c.login(username='user2', password='user2_password')
        response = c.get('/images/album/{}/'.format(album.id))
        assert response.status_code == 404

    def test_album_public(self):
        user = User.objects.get(username='user1')
        album = AlbumFactory.create(user=user, published='Public')
        album.save()
        c = Client()
        c.login(username='user2', password='user2_password')
        response = c.get('/images/album/{}/'.format(album.id))
        self.assertEqual(response.status_code, 200)
        self.assertIn(album.title, response.content)


class PhotoViewTestCase(TestCase):
    def setUp(self):
        user = UserFactory.create(username='user1')
        user.set_password('user1_password')
        user.save()
        user2 = UserFactory.create(username='user2')
        user2.set_password('user2_password')
        user2.save()
        photo = PhotoFactory.create(user=user)
        photo.save()

    def test_photo_view(self):
        photo = Photo.objects.all()[0]
        c = Client()
        c.login(username='user1', password='user1_password')
        response = c.get('/images/photos/{}/'.format(photo.id))
        self.assertIn(photo.title, response.content)
        self.assertIn(photo.description, response.content)

    def test_photo_nonuser(self):
        photo = Photo.objects.all()[0]
        c = Client()
        c.login(username='user2', password='user2_password')
        response = c.get('/images/photos/{}/'.format(photo.id))
        assert response.status_code == 404

    def test_photo_public(self):
        user = User.objects.get(username='user1')
        photo = PhotoFactory.create(user=user, published='Public')
        photo.save()
        c = Client()
        c.login(username='user2', password='user2_password')
        response = c.get('/images/photos/{}/'.format(photo.id))
        self.assertEqual(response.status_code, 200)
        self.assertIn(photo.title, response.content)


class LibraryViewTestCase(TestCase):
    def setUp(self):
        user = UserFactory.create(username='user1')
        user.set_password('user1_password')
        user.save()
        cover = PhotoFactory.create(user=user)
        cover.save()
        album = AlbumFactory.create(cover=cover, user=user)
        album.save()
        album.photos.add(cover)

    def test_library_view(self):
        photo = Photo.objects.all()[0]
        album = Album.objects.all()[0]
        c = Client()
        c.login(username='user1', password='user1_password')
        response = c.get('/images/library/')
        self.assertIn(photo.title, response.content)
        self.assertIn(album.title, response.content)

    def test_library_view_nonuser(self):
        photo = Photo.objects.all()[0]
        album = Album.objects.all()[0]
        c = Client()
        c.login(username='user2', password='user2_password')
        response = c.get('/images/library/')
        self.assertNotIn(photo.title, response.content)
        self.assertNotIn(album.title, response.content)
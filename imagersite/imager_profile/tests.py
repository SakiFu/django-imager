from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.test import TestCase
import factory
from imager_images.tests import PhotoFactory, AlbumFactory
from django.test import Client
from .models import ImagerProfile


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user{}".format(n))
    email = factory.Sequence(lambda n: "user{}@example.com".format(n))


class ProfileTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.build()
        self.user1 = UserFactory.build()
        self.user2 = UserFactory.build()

    def test_profile_is_created_when_user_is_saved(self):
        self.assertTrue(ImagerProfile.objects.count() == 0)
        self.user.save()
        self.user2.save()
        self.assertTrue(ImagerProfile.objects.count() == 2)

    def test_profile_str_is_user_username(self):
        self.user.save()
        profile = ImagerProfile.objects.get(user=self.user)
        self.assertEqual(str(profile), self.user.username)

    def test_profile_is_active(self):
        self.user.save()
        self.profile = ImagerProfile.objects.all()[0]
        self.assertTrue(self.profile.is_active)

    def test_profile_is_deleted(self):
        self.user.save()
        self.user.delete()
        self.assertTrue(ImagerProfile.objects.count() == 0)


class ProfileViewTestCase(TestCase):
    def setUp(self):
        user = UserFactory(username='user1')
        user.set_password('user1_password')
        user.save()
        user.profile.camera = 'NikonXXX'
        user.profile.address = 'Seattle'
        user.profile.website = 'www.user1.com'
        user.profile.photography_type = 'Animal'
        PhotoFactory(title='user1_photo', user=user)
        AlbumFactory(title='user1_album', user=user)
        user.profile.save()

        user2 = UserFactory(username='user2')
        user2.set_password('user1_password')
        user2.save()

    def test_view_profile(self):
        c = Client()
        c.login(username='user1', password='user1_password')
        response = c.get('/profile/')
        self.assertIn('NikonXXX', response.content)
        self.assertIn('Seattle', response.content)
        self.assertIn('Animal', response.content)

    def test_view_profile_other_user(self):
        c = Client()
        c.login(username='user2', password='user2_password')
        response = c.get('/profile/')
        self.assertNotIn('user1', response.content)
        self.assertNotIn('NikonXXX', response.content)
        self.assertNotIn('Seattle', response.content)
        self.assertNotIn('Animal', response.content)
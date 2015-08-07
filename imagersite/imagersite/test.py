from django.contrib.auth.models import User
from imager_images.models import Photo
from django.core import mail
from django.test import Client, TestCase
from imager_profile.models import ImagerProfile
import factory


class UserFactory(factory.Factory):
    class Meta:
        model = User
    first_name = 'jane'
    email = 'janedoe@example.com'
    username = 'janedoe123'


class PhotoFactory(factory.Factory):
    class Meta:
        model = Photo


class HomePageExists(TestCase):
    def setUp(self):
        self.c = Client()

    def test_homepage_exists(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)


class Login(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = UserFactory.create()
        self.user.set_password('password')
        self.user.save()

    def test_login_exist(self):
        response = self.c.get('/accounts/login/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_valid_user_login(self):
        self.c = Client()
        response = self.c.post(
            '/accounts/login/',
            {'username': self.user.username,
             'password': 'password'},
            follow=True)
        self.assertIn(self.user.username, response.content)

    def test_invalid_user_login(self):
        self.c = Client()
        response = self.c.post(
            '/accounts/login/',
            {'username': 'nobody',
             'password': 'password'},
            follow=True)
        self.assertIn('Invalid log in. Please try again!', response.content)


class Logout(TestCase):
    def setUp(self):
        self.c = Client()

    def test_logout_exit(self):
        response = self.c.get('/accounts/logout/', follow=True)
        self.assertEqual(response.status_code, 200)


class RegisterUser(TestCase):
    def setUp(self):
        self.user = UserFactory.create()
        self.user.set_password('password')
        self.user.save()

    def test_register_user_and_send_email(self):
        self.c = Client()
        response = self.c.post(
            '/accounts/register/',
            {'username': 'janedoe1234',
             'email': 'janedoe2@example.com',
             'password1': 'password',
             'password2': 'password'},
            follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Please check your email to complete the registration '
                      'process', response.content)
        imager_profile = ImagerProfile.objects.get(
            user__username='janedoe1234')
        self.assertEqual(imager_profile.is_active(), False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('Account activation', mail.outbox[0].subject)

    def test_name_already_registered(self):
        self.c = Client()
        response = self.c.post(
            '/accounts/register/',
            {'username': 'janedoe123',
             'email': 'janedoe@example.com',
             'password1': 'password',
             'password2': 'password'},
            follow=True)
        self.assertIn('A user with that username already exists.',
                      response.content)
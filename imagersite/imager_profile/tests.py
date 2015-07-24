from django.test import TestCase
from django.test import TestCase
import factory

from imager_profile.models import ImagerProfile

# Create your tests here.

class UserFactory(factory, Factory):
    class Meta:
        model = User

    username = factory.sequence([lambda n: 'user{}'.format(n))
    email = factory.Sequence([lambda n: 'user{}@example.com'.format(n))

class ProfileTestCases(TestCase):
    def setup(self):
        self.users = []
        self.user = UserFactory.build()
        for i in range():
            user = userFactory

    def test_profile_is_created_when_used_is_saved(self):
        self.assertTrue(ImageProfile.objects.count() == 0)

    def test_profile_str_is_user_username(self):
        self.user.save()
        profile = ImageProfile()
        self.assertEqual(str(profile) == True)
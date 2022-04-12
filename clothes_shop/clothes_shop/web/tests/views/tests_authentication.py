from django import test as django_test
from django.contrib.auth import get_user_model

from clothes_shop.web.helpers import ProfileDataMixin

UserModel = get_user_model()


class UserRegistrationViewTests(ProfileDataMixin, django_test.TestCase):

    def test_if_user_is_logged_in_successful(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        self.client.login(**self.VALID_USER_CREDENTIALS)
        self.assertTrue(user.is_authenticated)

from django import test as django_test
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.urls import reverse

from clothes_shop.web.helpers import ProfileDataMixin

UserModel = get_user_model()


class UserRegistrationViewTests(ProfileDataMixin, django_test.TestCase):
    INVALID = {
        'email': 'test',
        'password': '12345',
    }

    def test_create_profile__when_all_valid__expect_to_create(self):
        user = self.client.post(reverse('register'), data=self.VALID_USER_CREDENTIALS)
        profile = UserModel.objects
        self.assertIsNotNone(profile)

    def test_if_user_is_logged_in_successful(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        self.client.login(**self.VALID_USER_CREDENTIALS)
        self.assertTrue(user.is_authenticated)

    def test_if_it_renders_correct_template(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        self.client.login(**self.VALID_USER_CREDENTIALS)
        request = self.client.get(reverse('index'))
        self.assertEqual(request.status_code, 200)
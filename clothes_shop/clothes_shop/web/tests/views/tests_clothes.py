from django import test as django_test
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.urls import reverse

from clothes_shop.web.helpers import ProfileDataMixin, ClothesDataMixin
from clothes_shop.web.models import Clothes

UserModel = get_user_model()


class ClothesDetailViewTests(ProfileDataMixin, ClothesDataMixin, django_test.TestCase):

    def test_when_user_is_owner__expect_is_owner_to_be_true(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        self.client.login(**self.VALID_USER_CREDENTIALS)

        clothes = Clothes.objects.create(
            **self.VALID_CLOTHES_CREDENTIALS,
            user=user,
        )

        response = self.client.get(reverse('shop single', kwargs={'pk': clothes.pk}))

        self.assertTrue(response.context['is_owner'])

    def test_when_opening__not_existing_clothes_detail_page__expect_404(self):
        response = self.client.get(reverse('shop single', kwargs={'pk': 15}))

        self.assertEqual(response.status_code, 404)

    def test_recipe_title__when_valid_expect_correct_name(self):
        my_clothes = Clothes(**self.VALID_CLOTHES_CREDENTIALS)

        expected_clothes_title = f'{self.VALID_CLOTHES_CREDENTIALS["title"]}'
        expected_clothes_price = self.VALID_CLOTHES_CREDENTIALS['price']

        self.assertEqual(f'{expected_clothes_title} -> {expected_clothes_price:.2f}', my_clothes.__str__())

    def test_title_max_length(self):
        my_clothes = Clothes(**self.VALID_CLOTHES_CREDENTIALS)
        max_length = my_clothes._meta.get_field('title').max_length
        self.assertEqual(max_length, 30)

    def test_if_user_is_logged_in_successful(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        self.client.login(**self.VALID_USER_CREDENTIALS)
        self.assertTrue(user.is_authenticated)

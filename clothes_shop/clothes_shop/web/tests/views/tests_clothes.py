from django import test as django_test
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

    def test_clothes_title__when_valid_expect_correct_name(self):
        my_clothes = Clothes(**self.VALID_CLOTHES_CREDENTIALS)

        expected_clothes_title = f'{self.VALID_CLOTHES_CREDENTIALS["title"]}'
        expected_clothes_price = self.VALID_CLOTHES_CREDENTIALS['price']

        self.assertEqual(f'{expected_clothes_title} -> {expected_clothes_price:.2f}', my_clothes.__str__())

    def test_if_user_can_view_new_clothes_single_page(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)

        self.client.login(**self.VALID_USER_CREDENTIALS)

        my_clothes = Clothes.objects.create(
            **self.VALID_CLOTHES_CREDENTIALS,
            user=user,
        )
        response = self.client.get(reverse('shop single', kwargs={'pk': my_clothes.pk}))

        self.assertEqual(response.status_code, 200)


class EditClothesViewTests(ProfileDataMixin, ClothesDataMixin, django_test.TestCase):

    def test_if_edited_title_is_correctly_saved(self):
        my_clothes = Clothes(**self.VALID_CLOTHES_CREDENTIALS)
        my_clothes.title = 'NewTitle'
        self.assertEqual('NewTitle', my_clothes.title)

    def test_expect_correct_template(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        my_clothes = Clothes.objects.create(**self.VALID_CLOTHES_CREDENTIALS, user=user)
        self.client.get(reverse('edit_clothing', kwargs={'pk': my_clothes.pk}))
        self.assertTemplateUsed('clothes/edit-clothes.html')

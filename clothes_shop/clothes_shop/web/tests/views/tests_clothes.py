from django import test as django_test
from django.contrib.auth import get_user_model
from django.urls import reverse

from clothes_shop.web.helpers import ProfileDataMixin, ClothesDataMixin
from clothes_shop.web.models import Clothes
from clothes_shop.web.views.clothes_views import ShowClothesShopView

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


class ShowClothesShopViewTests(ProfileDataMixin, ClothesDataMixin, django_test.TestCase):
    def setUp(self) -> None:
        self.factory = django_test.RequestFactory()
        self.user = UserModel.objects.create(**self.VALID_USER_CREDENTIALS)

    def test_when_render_the_correct_template(self):
        request = self.factory.get('clothes-shop/')
        request.user = self.user
        response = ShowClothesShopView.as_view()(request)

        self.assertEqual(response.status_code, 200)

    def test_when_there_are_clothes__expect_clothes(self):
        self.clothes = Clothes.objects.create(
            **self.VALID_CLOTHES_CREDENTIALS,
            user=self.user
        )
        request = self.factory.get('clothes-shop/')
        request.user = self.user
        response = ShowClothesShopView.as_view()(request)

        self.assertEqual(response.context_data['all_clothes'][0], self.clothes)
        self.assertEqual(len(response.context_data['all_clothes']), 1)

    def test_when_there_are_no_clothes__expect_empty(self):
        request = self.factory.get('clothes-shop/')
        request.user = self.user
        response = ShowClothesShopView.as_view()(request)

        self.assertEqual(0, len(response.context_data['all_clothes']))

    def test_when_delete_clothes__expect_len_0(self):
        self.clothes = Clothes.objects.create(
            **self.VALID_CLOTHES_CREDENTIALS,
            user=self.user
        )
        request = self.factory.get('clothes-shop/')
        request.user = self.user
        response = ShowClothesShopView.as_view()(request)

        self.clothes.delete()
        self.assertEqual(len(response.context_data['all_clothes']), 0)
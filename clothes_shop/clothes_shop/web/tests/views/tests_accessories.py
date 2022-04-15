from django import test as django_test
from django.contrib.auth import get_user_model
from django.urls import reverse

from clothes_shop.web.helpers import ProfileDataMixin, AccessoriesDataMixin
from clothes_shop.web.models import Clothes, Accessories
from clothes_shop.web.views.accessories_views import ShowAccessoriesShopView

UserModel = get_user_model()


class AccessoriesDetailViewTests(ProfileDataMixin, AccessoriesDataMixin, django_test.TestCase):

    def test_when_user_is_owner__expect_is_owner_to_be_true(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        self.client.login(**self.VALID_USER_CREDENTIALS)

        accessory = Accessories.objects.create(
            **self.VALID_ACCESSORIES_DATA,
            user=user,
        )

        response = self.client.get(reverse('accessories-shop single', kwargs={'pk': accessory.pk}))

        self.assertTrue(response.context['is_owner'])

        self.assertTrue(response.context['is_owner'])

    def test_clothes_title__when_valid_expect_correct_name(self):
        accessory = Accessories(**self.VALID_ACCESSORIES_DATA)

        expected_clothes_title = f'{self.VALID_ACCESSORIES_DATA["title"]}'
        expected_clothes_price = self.VALID_ACCESSORIES_DATA['price']

        self.assertEqual(f'{expected_clothes_title} -> {expected_clothes_price:.2f}', accessory.__str__())

    def test_if_user_can_view_new_clothes_single_page(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)

        self.client.login(**self.VALID_USER_CREDENTIALS)

        accessory = Accessories.objects.create(
            **self.VALID_ACCESSORIES_DATA,
            user=user,
        )
        response = self.client.get(reverse('accessories-shop single', kwargs={'pk': accessory.pk}))

        self.assertEqual(response.status_code, 200)


class EditAccessoriesViewTests(ProfileDataMixin, AccessoriesDataMixin, django_test.TestCase):

    def test_if_edited_title_is_correctly_saved(self):
        my_clothes = Accessories(**self.VALID_ACCESSORIES_DATA)
        my_clothes.title = 'NewTitle'
        self.assertEqual('NewTitle', my_clothes.title)

    def test_expect_correct_template(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        accessory = Accessories.objects.create(**self.VALID_ACCESSORIES_DATA, user=user)
        self.client.get(reverse('edit_accessories', kwargs={'pk': accessory.pk}))
        self.assertTemplateUsed('accessories/edit-accessories.html')


class ShowAccessoriesShopViewTests(ProfileDataMixin, AccessoriesDataMixin, django_test.TestCase):
    def setUp(self) -> None:
        self.factory = django_test.RequestFactory()
        self.user = UserModel.objects.create(**self.VALID_USER_CREDENTIALS)

    def test_when_render_the_correct_template(self):
        request = self.factory.get('accessories-shop/')
        request.user = self.user
        response = ShowAccessoriesShopView.as_view()(request)

        self.assertEqual(response.status_code, 200)

    def test_when_there_are_accessories__expect_accessories(self):
        self.clothes = Accessories.objects.create(
            **self.VALID_ACCESSORIES_DATA,
            user=self.user
        )
        request = self.factory.get('accessories-shop/')
        request.user = self.user
        response = ShowAccessoriesShopView.as_view()(request)

        self.assertEqual(response.context_data['all_accessories'][0], self.clothes)
        self.assertEqual(len(response.context_data['all_accessories']), 1)

    def test_when_there_are_no_accessories__expect_empty(self):
        request = self.factory.get('accessories-shop/')
        request.user = self.user
        response = ShowAccessoriesShopView.as_view()(request)

        self.assertEqual(0, len(response.context_data['all_accessories']))

    def test_when_delete_accessories__expect_len_0(self):
        self.clothes = Accessories.objects.create(
            **self.VALID_ACCESSORIES_DATA,
            user=self.user
        )
        request = self.factory.get('accessories-shop/')
        request.user = self.user
        response = ShowAccessoriesShopView.as_view()(request)

        self.clothes.delete()
        self.assertEqual(len(response.context_data['all_accessories']), 0)

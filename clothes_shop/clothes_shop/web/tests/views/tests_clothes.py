from django import test as django_test
from django.contrib.auth import get_user_model
from django.urls import reverse

from clothes_shop.web.models import Clothes

UserModel = get_user_model()


class ClothesDetailViewTests(django_test.TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'test@abv.bg',
        'password': '12345',
    }

    VALID_CLOTHES_CREDENTIALS = {
        'title': 'MyClothes',
        'clothes_type': 'Jeans',
        'materials': 'Cotton',
        'description': 'dasdasd',
        'image': 'http://cat.png',
        'price': 143,
    }

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
        response = self.client.get(reverse('shop single', kwargs={'pk': 10}))

        self.assertEqual(response.status_code, 404)

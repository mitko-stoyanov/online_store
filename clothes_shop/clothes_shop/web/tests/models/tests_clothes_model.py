from django import test as django_test
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from clothes_shop.web.helpers import ProfileDataMixin, ClothesDataMixin
from clothes_shop.web.models import Clothes

UserModel = get_user_model()


class ClothesDetailViewTests(ProfileDataMixin, ClothesDataMixin, django_test.TestCase):

    def test_if_price_validator_works(self):
        my_clothes = Clothes(**self.VALID_CLOTHES_CREDENTIALS)
        my_clothes.price = -5
        with self.assertRaises(ValidationError) as context:
            my_clothes.full_clean()
            my_clothes.save()
        self.assertIsNotNone(context.exception)
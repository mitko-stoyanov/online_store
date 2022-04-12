from django.test import TestCase

from clothes_shop.web.models import Shoes


class ShoesTests(TestCase):
    VALID_SHOES_DATA = {
        'title': 'NewShoes',
        'size': 4,
        'price': 134,
        'shoes_type': 'Sandals',
        'suitable_for': 'Summer',
        'description': 'dsadas',
        'image': 'https://media.istockphoto.com/vectors/the-driver-license-is-an-icon-vector-isolated-contour-symbol'
                 '-vector-id1206172182?k=20&m=1206172182&s=170667a&w=0&h=4OwnFq2u86X9r0nftxEzvt9Zw-aa_A7awlz_c1Now2g=',
        'user_id': 9,
    }

    def test_add_shoes__when_title_contains_only_letters__expect_to_success(self):
        shoes = Shoes(**self.VALID_SHOES_DATA, )
        shoes.full_clean()
        shoes.save()

    def test_add_shoes__when_title_contains_a_digit__expect_to_fail(self):
        pass

    def test_add_shoes__when_title_contains_a_space__expect_to_fail(self):
        pass

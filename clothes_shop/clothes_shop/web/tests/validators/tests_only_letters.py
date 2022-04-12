from django.core.exceptions import ValidationError
from django.test import TestCase

from clothes_shop.web.validators import validate_only_letters


class ValidateOnlyLettersTest(TestCase):
    def test_when_there_is_digits__expect_to_raise_ValidationError(self):
        value = 'testcode123'
        with self.assertRaises(ValidationError):
            validate_only_letters(value)

    def test_when_there_is_space__expect_to_raise_ValidationError(self):
        value = 'test code'
        with self.assertRaises(ValidationError):
            validate_only_letters(value)

    def test_when_there_is_only_letters_expect_to_do_nothing(self):
        value = 'testcode'
        self.assertEqual(None, validate_only_letters(value))

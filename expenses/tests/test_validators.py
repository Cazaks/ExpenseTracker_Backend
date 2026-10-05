from django.test import SimpleTestCase
from django.core.exceptions import ValidationError

from expenses.validators import SpecialCharacterValidator, NoWhiteSpaceValidator
from expenses.validators import UppercaseValidator


class SpacialCharacterValidatorTests(SimpleTestCase):
    def setUp(self):
        self.validator = SpecialCharacterValidator()

    def test_password_with_special_char_passes(self):
        self.validator.validate("myp@assword")

    def test_password_without_special_char_fails(self):
        with self.assertRaises(ValidationError):
            self.validator.validate("mypassword")


class NoWhiteSpaceValidatorTests(SimpleTestCase):
    def setUp(self):
        self.validator = NoWhiteSpaceValidator()

    def test_password_without_whitespace_passes(self):
        self.validator.validate("myp@assword")

    def test_password_with_whitespace_fails(self):
        with self.assertRaises(ValidationError):
            self.validator.validate("my p@assword")


class UpperCaseValidatorTests(SimpleTestCase):
    def setUp(self):
        self.validator = UppercaseValidator()

    def test_password_with_uppercase_passes(self):
        self.validator.validate("myp@assworD23")

    def test_password_without_uppercase_fails(self):
        with self.assertRaises(ValidationError):
            self.validator.validate("myp@assword23")
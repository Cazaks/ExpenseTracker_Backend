from unittest import TestCase

from expenses.validators import SpecialCharacterValidator, NoWhiteSpaceValidator
from expenses.validators import UppercaseValidator


class SpacialCharacterValidatorTests(TestCase):
    def setUp(self):
        self.validator = SpecialCharacterValidator()

    def test_password_with_special_char_passes(self):
        self.validator.validate("myp@assword")

    def test_password_without_special_char_fails(self):
        self.validator.validate("mypassword")


class NoWhiteSpaceValidatorTests(TestCase):
    def setUp(self):
        self.validator = NoWhiteSpaceValidator()

    def test_password_without_whitespace_passes(self):
        self.validator.validate("myp@assword")

    def test_password_with_whitespace_fails(self):
        self.validator.validate("my p@assword")

class UpperCaseValidatorTests(TestCase):
    def setUp(self):
        self.validator = UppercaseValidator()

    def test_password_with_uppercase_passes(self):
        self.validator.validate("myp@assworD23")

    def test_password_without_uppercase_fails(self):
        with self.assertRaises(ValueError):
            self.validator.validate("myp@assword23")





from unittest import TestCase

from ExpenseTracker_Backend.expenses.validators import SpecialCharacterValidator, NoWhiteSpaceValidator


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



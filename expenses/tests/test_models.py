from django.contrib.auth.models import User
from django.test import TestCase
from expenses.models import Category


class CategoryModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="ada", password="Myp@ssword1")

    def test_category_str_returns_name(self):
        category = Category.objects.create(user=self.user, category_name="Food")
        self.assertEqual(str(category), "Food")

    def test_category_is_active_defaults_to_true(self):
        category = Category.objects.create(user=self.user, category_name="Transport")
        self.assertTrue(category.is_active)

    def test_category_requires_a_user(self):
        category = Category(category_name="Rent")
        with self.assertRaises(Exception):
            category.full_clean()


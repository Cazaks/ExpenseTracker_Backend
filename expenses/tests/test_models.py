from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from expenses.models import Category, Expense


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

class ExpenseModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="ada", password="Myp@ssword1")
        self.category = Category.objects.create(user=self.user, category_name="Food")

    def test_expense_str_shows_amount_and_description(self):
        expense = Expense.objects.create(
            user=self.user, category=self.category, amount=Decimal("45.00"),
            description="Lunch", date=timezone.localdate(),
        )
        self.assertEqual(str(expense), "45.00 - Lunch")

    def test_expense_created_at_is_set_automatically(self):
        expense = Expense.objects.create(
            user=self.user, category=self.category,
            amount=Decimal("10.00"), date=timezone.localdate(),
        )
        self.assertIsNotNone(expense.created_at)


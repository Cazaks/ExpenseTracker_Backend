from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from expenses.models import Category


class CategoryAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Udo', password='myp@ssworD23')
        self.other_user = User.objects.create_user(username='Agbi', password='anothErPassword@1')
        self.client.force_authenticate(user=self.user)

    def test_create_category_successfully(self):
        response = self.client.post("/api/categories/", {"category_name": "Food", "color": "#FF5733"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.first().user, self.user)

    def test_create_category_with_blank_name_fails(self):
        response = self.client.post("/api/categories/", {"category_name": "   "})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_cannot_see_another_users_categories(self):
        Category.objects.create(user=self.other_user, category_name="Rent")
        response = self.client.get("/api/categories/")
        self.assertEqual(len(response.data), 0)

    def test_unauthenticated_request_is_rejected(self):
        self.client.force_authenticate(user=None)
        response = self.client.get("/api/categories/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_category_soft_deletes_instead_of_removing(self):
        category = Category.objects.create(user=self.user, category_name="Food")
        response = self.client.delete(f"/api/categories/{category.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        category.refresh_from_db()
        self.assertFalse(category.is_active)
        self.assertTrue(Category.objects.filter(id=category.id).exists())

        response = self.client.get("/api/categories/")
        self.assertEqual(len(response.data), 0)

class SignupAPITests(APITestCase):
    def test_signup_creates_user(self):
        response = self.client.post("/api/signup/", {
            "username": "newuser",
            "email": "new@example.com",
            "password": "Myp@ssword1",
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="newuser").exists())
        self.assertNotIn("password", response.data)

    def test_signup_rejects_weak_password(self):
        response = self.client.post("/api/signup/", {
            "username": "weakuser",
            "email": "weak@example.com",
            "password": "password",
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
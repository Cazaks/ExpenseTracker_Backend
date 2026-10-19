from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import CategoryViewSet, SignUpView, ExpenseViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="category")
router.register("expenses", ExpenseViewSet, basename="expense")

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
] + router.urls
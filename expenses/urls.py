from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import CategoryViewSet, SignUpView

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="category")

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
] + router.urls
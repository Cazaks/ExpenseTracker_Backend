from decimal import Decimal

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import Category, Expense


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'color', 'is_active']
        read_only_fields = ['id']

    def validate_category_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Category name cannot be blank.")
        return value


class SignUpSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        read_only_fields = ['id']

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user


class OwnedCategoryField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request')
        if request is None or not request.user.is_authenticated:
            return Category.objects.none()
        return Category.objects.filter(user = request.user, is_active=True)

    def to_representation(self, value):
        return str(value.pk)


class ExpenseSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    category = OwnedCategoryField()

    class Meta:
        model = Expense
        fields = ['id', 'category', 'amount', 'description',
                  'date', 'payment_method', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_amount(self, value):
        if value <= Decimal ("0"):
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value





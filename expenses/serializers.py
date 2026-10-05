from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'color', 'is_deleted']
        read_only_fields = ['id']

    def validate_category_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Category name cannot be blank.")
        return value
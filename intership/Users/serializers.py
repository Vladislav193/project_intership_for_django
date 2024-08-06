from rest_framework import serializers
from .models import User, Division


class CustomUserSerializer(serializers.ModelSerializer):
    """Сериализатор для users"""
    class Meta:
        model = User
        fields = ("name", "last_name", "login", "email",
                  "password", "division")


class DivisionSerializer(serializers.ModelSerializer):
    """Сериализатор для заполенение отделов"""
    class Meta:
        model = Division
        fields = ("name", "director")
from rest_framework import serializers
from .models import User, Division

class DivisionSerializer(serializers.ModelSerializer):
    """Сериализатор для заполенение отделов"""
    class Meta:
        model = Division
        fields = ("name", "director")


class CustomUserSerializer(serializers.ModelSerializer):
    """Сериализатор для users"""
    division = DivisionSerializer()
    class Meta:
        model = User
        fields = ("name", "last_name", "login", "email",
                  "password", "division")



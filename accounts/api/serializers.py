from rest_framework import serializers
from rest_auth.serializers import LoginSerializer
from rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model

from accounts.models import Cart

User = get_user_model()


class CustomLoginSerializer(LoginSerializer):
    username = None
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={"input_type": "password"})

    class Meta:
        model = User
        fields = ["email", "password"]


class CustomRegistrationSerializer(RegisterSerializer):
    username = None
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["pk", "email", "first_name", "last_name", "phone", "date_of_birth", "picture", "last_login"]
        read_only_fields = ["pk", "email", "last_login"]


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = [""]

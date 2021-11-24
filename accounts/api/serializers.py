from rest_framework import serializers
from rest_auth.serializers import LoginSerializer
from rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model

from accounts.models import (
    Cart,
    ProductCart,
    UserFavorite,
    UserShopped,
    UserAccessed,
    UserAddresses,
    ProductUserAccessed
)
from products.api.serializers import ProductListSerializer

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
        fields = ["id", "email", "first_name", "last_name", "phone", "date_of_birth", "picture", "last_login"]
        read_only_fields = ["id", "email", "last_login"]


class ProductCartSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(many=False, read_only=True)

    class Meta:
        model = ProductCart
        fields = ["id", "quantity", "sum_freight", "sum_price", "product"]
        read_only_fields = ["id", "product", "sum_freight", "sum_price"]


class CartSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(many=False, read_only=True)
    products_cart = ProductCartSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "total_freight", "subtotal", "total", "user", "products_cart"]
        read_only_fields = fields


class UserFavoriteSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = UserFavorite
        fields = ["id", "products"]
        read_only_fields = fields


class UserShoppedSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = UserShopped
        fields = ["id", "products"]
        read_only_fields = fields


class ProductUserAccessedSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(many=False, read_only=True)

    class Meta:
        model = ProductUserAccessed
        fields = ["id", "hit", "product"]
        read_only_fields = ["id", "product"]


class UserAccessedSerializer(serializers.ModelSerializer):
    user_accessed_product = ProductUserAccessedSerializer(many=True, read_only=True)

    class Meta:
        model = UserAccessed
        fields = ["id", "user_accessed_product"]
        read_only_fields = fields


class UserAddressesSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAddresses
        fields = [
            "id", "user", "identification", "zip_code", "recipient", "phone", "address", "number", "complement",
            "reference", "neighborhood", "city", "state", "is_default"
        ]
        read_only_fields = ["id"]

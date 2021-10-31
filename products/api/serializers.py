from rest_framework import serializers
from products.models import (
    Category,
    Product,
    Characteristic
)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name", "image", "alt_image"]


class CharacteristicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Characteristic
        fields = ["id", "name", "description"]


class ProductDetailSerializer(serializers.ModelSerializer):
    characteristics = CharacteristicSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    access = serializers.IntegerField(source="access.hit", read_only=True)
    sale = serializers.IntegerField(source="sale.hit", read_only=True)

    class Meta:
        model = Product
        fields = [
            "id", "name", "description", "price", "image", "alt_image", "access", "sale", "characteristics",
            "categories"
        ]
        read_only_fields = fields


class ProductListSerializer(serializers.ModelSerializer):
    access = serializers.IntegerField(source="access.hit", read_only=True)
    sale = serializers.IntegerField(source="sale.hit", read_only=True)

    class Meta:
        model = Product
        fields = ["id", "name", "price", "image", "alt_image", "access", "sale"]
        read_only_fields = fields

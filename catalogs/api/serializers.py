from rest_framework import serializers
from catalogs.models import Catalog
from products.api.serializers import ProductListSerializer


class CatalogSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = Catalog
        fields = ["id", "name", "description", "image", "alt_image", "products"]
        read_only_fields = fields

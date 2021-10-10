from rest_framework import serializers
from products.models import (
    Category,
    Product,
    Access,
    Sale,
    Characteristic
)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ["id", "name"]

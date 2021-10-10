from rest_framework import serializers
from managements.models import (
    Banner,
    Promotion,
    Home
)
from products.api.serializers import CategorySerializer
from posts.api.serializers import PostListSerializer


class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        fields = ["id", "link", "image", "alt_image"]
        read_only_fields = fields


class PromotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promotion
        fields = ["id", "link", "image", "alt_image"]
        read_only_fields = fields


class HomeSerializer(serializers.ModelSerializer):
    banner = BannerSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    promotions = PromotionSerializer(many=True, read_only=True)
    posts = PostListSerializer(many=True, read_only=True)

    class Meta:
        model = Home
        fields = ["title", "subtitle", "most_acessed", "most_sold", "most_favorite", "banner", "categories",
                  "promotions", "posts"]
        read_only_fields = fields

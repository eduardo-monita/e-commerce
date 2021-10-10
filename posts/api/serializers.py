from rest_framework import serializers
from posts.models import Author, Post


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ["id", "email", "first_name", "last_name", "picture", "alt_picture"]
        read_only_fields = fields


class PostListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False, read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "summary", "image", "alt_image", "author"]
        read_only_fields = fields


class PostDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False, read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "subtitle", "summary", "image", "alt_image", "body", "author"]
        read_only_fields = fields

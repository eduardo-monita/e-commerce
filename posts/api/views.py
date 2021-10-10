from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from posts.models import Author, Post
from posts.api.serializers import (
    AuthorSerializer,
    PostListSerializer,
    PostDetailSerializer
)


@permission_classes([IsAuthenticated])
class AuthorView(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    http_method_names = ["get", "head"]

    def get_queryset(self):
        return Author.objects.actives()


@permission_classes([IsAuthenticated])
class PostView(viewsets.ModelViewSet):
    http_method_names = ["get", "head"]
    serializers = {
        "default": PostListSerializer,
        "list": PostListSerializer,
        "retrieve": PostDetailSerializer,
    }

    def get_queryset(self):
        return Post.objects.actives().order_by("-created_at")

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers.get("default"))

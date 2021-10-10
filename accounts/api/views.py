from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.generics import RetrieveUpdateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated

from accounts.api.serializers import (
    CartSerializer,
    UserAccessedSerializer,
    UserDetailSerializer,
    ProductCartSerializer,
    UserFavoriteSerializer,
    UserShoppedSerializer
)
from accounts.models import (
    Cart,
    ProductCart,
    UserFavorite,
    UserShopped,
    UserAccessed,
    ProductUserAccessed
)

User = get_user_model()


@permission_classes([IsAuthenticated])
class UserDetailsView(RetrieveUpdateAPIView):
    serializer_class = UserDetailSerializer
    lookup_field = None

    def get_object(self):
        return self.request.user


@permission_classes([IsAuthenticated])
class CartView(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    http_method_names = ["get", "head"]

    def get_queryset(self):
        return Cart.objects.actives().filter(user=self.request.user)


@permission_classes([IsAuthenticated])
class ProductCartView(viewsets.ModelViewSet):
    serializer_class = ProductCartSerializer
    http_method_names = ["patch", "options", "delete"]

    def get_queryset(self):
        return ProductCart.objects.actives().filter(cart=self.kwargs.get('cart_pk'))


@permission_classes([IsAuthenticated])
class UserFavoriteView(viewsets.ModelViewSet):
    serializer_class = UserFavoriteSerializer
    http_method_names = ["get", "head"]

    def get_queryset(self):
        return UserFavorite.objects.actives().filter(user=self.request.user)


@permission_classes([IsAuthenticated])
class UserShoppedView(viewsets.ModelViewSet):
    serializer_class = UserShoppedSerializer
    http_method_names = ["get", "head"]

    def get_queryset(self):
        return UserShopped.objects.actives().filter(user=self.request.user)


@permission_classes([IsAuthenticated])
class UserAccessedView(viewsets.ModelViewSet):
    serializer_class = UserAccessedSerializer
    http_method_names = ["get", "head"]

    def get_queryset(self):
        return UserAccessed.objects.actives().filter(user=self.request.user)

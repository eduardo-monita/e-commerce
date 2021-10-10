from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.generics import RetrieveUpdateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from accounts.api.serializers import UserDetailSerializer
from accounts.models import Cart

User = get_user_model()


@permission_classes([IsAuthenticated])
class UserDetailsView(RetrieveUpdateAPIView):
    serializer_class = UserDetailSerializer
    lookup_field = None

    def get_object(self):
        return self.request.user


@permission_classes([IsAuthenticated])
class CartView(viewsets.ModelViewSet):
    # serializer_class = ContactSerializer
    http_method_names = ["get", "head"]

    def get_queryset(self):
        return Cart.objects.actives(user=self.request.user)

    @action(detail=True, methods=["post"])
    def add_product(self, request, *args, **kwargs):
        cart = get_object_or_404(Cart, id=kwargs.get("pk"))
        pass

    @action(detail=True, methods=["delete"])
    def remove_product(self, request, *args, **kwargs):
        cart = get_object_or_404(Cart, id=kwargs.get("pk"))
        pass

from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes, action
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from helpers.stripe import Stripe
from stripe.error import StripeError
from django.utils.translation import ugettext_lazy as _
from accounts.api.serializers import (
    CartSerializer,
    UserAccessedSerializer,
    UserDetailSerializer,
    ProductCartSerializer,
    UserFavoriteSerializer,
    UserShoppedSerializer,
    UserAddressesSerializer
)
from accounts.models import (
    Cart,
    ProductCart,
    UserFavorite,
    UserShopped,
    UserAccessed,
    UserAddresses
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
    http_method_names = ["get", "head", "post", "options"]

    def get_queryset(self):
        return Cart.objects.actives().filter(user=self.request.user)

    @action(detail=True, methods=['POST'])
    def finilize_cart(self, request, *args, **kwargs):
        """
        {
            "number": "2223003122003222",
            "exp_month": 11,
            "exp_year": 2022,
            "cvc": "000"
        }
        """
        try:
            cart = self.get_queryset().first()
            if int(cart.int_total()) > 0:
                data = request.data
                card_token = Stripe().gen_card_token(
                    data.get('number'), data.get('exp_month'), data.get('exp_year'), data.get('cvc')
                )
                Stripe().create_charge(card_token, cart.int_total(), f'{cart.user.email} - {cart.int_total()}')
                return Response(status=status.HTTP_200_OK, data={"message": _("Payment successfully processed!")})
            return Response(
                data={"error": _("To realize the payment need to be more than in your cart 0.50$")},
                status=status.HTTP_400_BAD_REQUEST
            )
        except StripeError as error:
            return Response(data={"error": error}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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


@permission_classes([IsAuthenticated])
class UserAddressesView(viewsets.ModelViewSet):
    serializer_class = UserAddressesSerializer
    http_method_names = ["get", "head", "post", "patch", "options", "delete"]

    def get_queryset(self):
        return UserAddresses.objects.actives().filter(user=self.request.user)

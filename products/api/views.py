from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django_filters import rest_framework as dj_filters
from rest_framework import viewsets, status, filters
from rest_framework.decorators import permission_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from accounts.api.serializers import CartSerializer, UserFavoriteSerializer
from accounts.models import Cart, ProductCart, UserAccessed, UserFavorite, UserShopped
from products.models import Access, Product, Category, Sale
from products.api.serializers import (
    CategorySerializer,
    ProductListSerializer,
    ProductDetailSerializer
)
from helpers.calculate_freight import calculate_feight


@permission_classes([IsAuthenticated])
class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    http_method_names = ["get", "head"]

    def get_queryset(self):
        return Category.objects.actives()


class ProductFilter(dj_filters.FilterSet):
    min_price = dj_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = dj_filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'categories']


class ProductPagination(LimitOffsetPagination):
    default_limit = None


@permission_classes([IsAuthenticated])
class ProductView(viewsets.ModelViewSet):
    filter_backends = [dj_filters.DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ["sale__hit", "access__hit", "user_favorite__count"]
    filterset_class = ProductFilter
    pagination_class = ProductPagination
    serializers = {
        "default": ProductListSerializer,
        "list": ProductListSerializer,
        "retrieve": ProductDetailSerializer,
    }
    http_method_names = ["get", "head", "post"]

    def get_queryset(self):
        return Product.objects.actives().annotate(Count("user_favorite"))

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers.get("default"))

    @action(detail=True, methods=['post'])
    def add_to_cart(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs.get('pk'))
        cart = get_object_or_404(Cart, user=request.user)
        product_cart = ProductCart.objects.actives().get_or_create(cart=cart, product=product)[0]
        product_cart.quantity += 1
        product_cart.save(update_fields=["quantity"])
        response_serializer = CartSerializer(Cart.objects.actives().get(user=request.user), many=False)
        return Response(data=response_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def remove_from_cart(self, request, *args, **kwargs):
        product_cart = get_object_or_404(ProductCart, cart__user=request.user, product=kwargs.get('pk'))
        product_cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['POST'])
    def add_to_favorites(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs.get('pk'))
        user_favorite = UserFavorite.objects.actives().get_or_create(user=request.user)[0]
        if not user_favorite.products.actives().filter(id=product.id).exists():
            user_favorite.products.add(product)
        response_serializer = UserFavoriteSerializer(user_favorite, many=False)
        return Response(data=response_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['POST'])
    def remove_from_favorites(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs.get('pk'))
        user_favorite = get_object_or_404(UserFavorite, user=request.user, products=product.id)
        user_favorite.products.remove(product)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['POST'])
    def hit_access(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs.get('pk'))
        access = Access.objects.actives().get_or_create(product=product)[0]
        access.hit += 1
        access.save(update_fields=["hit"])
        if request.user:
            user_accessed = UserAccessed.objects.actives().get_or_create(user=request.user)[0]
            if not user_accessed.products.actives().filter(id=product.id).exists():
                user_accessed.products.add(product)
        response_serializer = ProductListSerializer(product, many=False)
        return Response(data=response_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['POST'])
    def hit_sale(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs.get('pk'))
        sale = Sale.objects.actives().get_or_create(product=product)[0]
        sale.hit += 1
        sale.save(update_fields=["hit"])
        if request.user:
            user_shopped = UserShopped.objects.actives().get_or_create(user=request.user)[0]
            if not user_shopped.products.actives().filter(id=product.id).exists():
                user_shopped.products.add(product)
        response_serializer = ProductListSerializer(product, many=False)
        return Response(data=response_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['GET'])
    def calculate_freight(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs.get('pk'))
        if request.query_params.get("zip_code"):
            response_calc = calculate_feight(product, request.query_params.get("zip_code"))
            if response_calc is None:
                return Response(data={"error": _("Product unavaiable to this zip code")}, status=status.HTTP_200_OK)
            if response_calc[0].get("error"):
                return Response(data=response_calc, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(data=response_calc, status=status.HTTP_200_OK)
        return Response(data={"error": _("Zip code not informed!")}, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
class ProductCartView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    http_method_names = ["get", "head", "patch", "options"]

    def get_queryset(self):
        return ProductCart.objects.actives()

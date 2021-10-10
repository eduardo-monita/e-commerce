from django.db.models import Count
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as dj_filters
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import permission_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from accounts.models import Cart, ProductCart
from products.models import Product, Category
from products.api.serializers import (
    CategorySerializer,
    ProductListSerializer,
    ProductDetailSerializer
)


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
    http_method_names = ["get", "head"]

    def get_queryset(self):
        return Product.objects.actives().annotate(Count("user_favorite"))

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers.get("default"))

    # @action(detail=True, methods=['POST'])
    # def add_to_cart(self, request, *args, **kwargs):
    #     product = get_object_or_404(Product, id=kwargs.get('pk'))
    #     cart = Cart.objects.actives().get_or_create(user=request.user)
    #     product_cart = ProductCart.objects.actives().get_or_create(cart=cart)

    #     # serializer = (instance=budget, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     budget = self.get_object()
    #     response_serializer = serializers.BudgetCSEditSerializer(budget, context=self.get_serializer_context())
    #     pass

    @action(detail=True, methods=['POST'])
    def remove_from_cart(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs.get('pk'))
        pass

    @action(detail=True, methods=['POST'])
    def add_to_favorites(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs.get('pk'))
        pass

    @action(detail=True, methods=['POST'])
    def hit_access(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs.get('pk'))
        pass

    @action(detail=True, methods=['POST'])
    def hit_sale(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs.get('pk'))
        pass

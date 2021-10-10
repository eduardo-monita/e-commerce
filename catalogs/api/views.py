from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from catalogs.models import Catalog
from catalogs.api.serializers import CatalogSerializer


@permission_classes([IsAuthenticated])
class CatalogView(viewsets.ModelViewSet):
    serializer_class = CatalogSerializer
    http_method_names = ["get", "head"]

    def get_queryset(self):
        return Catalog.objects.actives()

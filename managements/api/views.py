from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from managements.models import Home
from managements.api.serializers import HomeSerializer


@permission_classes([IsAuthenticated])
class HomeView(viewsets.ModelViewSet):
    serializer_class = HomeSerializer
    http_method_names = ["get", "head"]

    def get_queryset(self):
        return Home.objects.actives()

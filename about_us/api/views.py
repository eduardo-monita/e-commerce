from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from about_us.api.serializers import CompanySerializer, ContactSerializer
from about_us.models import Company, Contact


@permission_classes([IsAuthenticated])
class CompanyView(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    http_method_names = ["get", "head"]

    def get_queryset(self):
        return Company.objects.actives()


@permission_classes([IsAuthenticated])
class ContactView(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    http_method_names = ["post"]

    def get_queryset(self):
        return Contact.objects.actives()

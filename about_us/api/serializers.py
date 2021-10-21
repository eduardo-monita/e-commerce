from rest_framework import serializers
from about_us.models import Company, Contact
from django.core.mail import send_mail


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = [
            "title", "description", "image", "alt_image", "description", "motivation", "principles", "address",
            "email", "phone", "cnpj", "origin_zip_code"
        ]
        read_only_fields = fields


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ["name", "email", "phone", "body"]

    def create(self, validated_data):
        created_data = super().create(validated_data)
        company = Company.objects.actives().first()
        if company:
            send_mail(
                f"E-commerce contact from name: {validated_data.get('name')}, phone: {validated_data.get('phone')}",
                validated_data.get("body"),
                validated_data.get("email"),
                [company.email],
                fail_silently=False,
            )
        return created_data

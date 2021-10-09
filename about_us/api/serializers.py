from rest_framework import serializers
from about_us.models import Company, Contact


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = [
            "title", "description" "image", "alt_image", "description", "motivation", "principles", "address",
            "email", "phone", "cnpj"
        ]


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ["name", "email", "phone", "body"]

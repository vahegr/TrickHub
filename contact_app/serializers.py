from rest_framework import serializers
from .models import ContactInformation


class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = (
            'phone', 'second_phone', 'third_phone',
            'email', 'instagram', 'whatsapp', 'allowing'
        )

from rest_framework import serializers
from .models import Service


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('title', 'description', 'icon')

from rest_framework import serializers
from .models import User
from django.utils import timezone


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email', 'username', 'full_name',
            'phone', 'image', 'bio', 'instagram',
            'github', 'linkedin', 'twitter')

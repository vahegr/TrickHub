from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id', 'parent', 'slug', 'user',
            'title', 'description', 'image',
            'created_at', 'jalali_created', 'hits')

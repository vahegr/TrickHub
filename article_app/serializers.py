from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id', 'parent', 'slug', 'user',
            'title', 'description', 'image',
            'created_at', 'jalali_created', 'hits')

        def get_image(self, obj):               # if view was ApiView this is necessary
            request = self.context.get('request')
            if obj.image:
                image_url = obj.image.url
                return request.build_absolute_uri(image_url)
            return None

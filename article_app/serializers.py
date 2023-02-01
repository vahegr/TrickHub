from rest_framework import serializers
from .models import Article, Comment, Like


class ArticleSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Article
        fields = (
            'id', 'parent', 'slug', 'user',
            'title', 'description', 'image',
            'created_at', 'jalali_created', 'hits', 'comments', 'likes')

    def get_image(self, obj):               # if view was ApiView this is necessary
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)
        return None

    def get_comments(self, obj):
        serializer = CommentSerializer(instance=obj.comments.all(), many=True)
        return serializer.data

    def get_likes(self, obj):
        serializer = LikeSerializer(instance=obj.likes.all(), many=True)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    
    class Meta:
        model = Comment
        fields = ('id', 'article', 'user', 'parent', 'comment', 'created_time', 'jalali_created')


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Like
        fields = ('id', 'article', 'user', 'created_at')

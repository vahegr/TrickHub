from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from account_app.permissions import OwnerOrRead
from .serializers import ArticleSerializer
from .models import Article


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.filter(allowing=True)
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.action in ['update', 'create', 'destroy', 'partial_update']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAdminUser, OwnerOrRead]
        return [permission() for permission in permission_classes]

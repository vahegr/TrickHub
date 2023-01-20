from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from account_app.permissions import OwnerOrRead
from .serializers import SampleSerializer
from .models import Sample


class SamplesViewSet(ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer

    def get_permissions(self):
        if self.action in ['update', 'create', 'destroy', 'partial_update']:
            permission_classes = [IsAdminUser]
            return [permission() for permission in permission_classes]

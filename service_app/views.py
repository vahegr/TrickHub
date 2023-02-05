from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .serializers import ServiceSerializer
from .models import Service


class ServicesViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_permissions(self):
        if self.action in ['update', 'create', 'destroy', 'partial_update']:
            self.permission_classes = [IsAdminUser, ]
        return super(ServicesViewSet, self).get_permissions()

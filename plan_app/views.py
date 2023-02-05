from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from account_app.permissions import OwnerOrRead
from .serializers import PlanSerializer
from .models import Plan


class PlansViewSet(ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

    def get_permissions(self):
        if self.action in ['update', 'create', 'destroy', 'partial_update']:
            self.permission_classes = [IsAdminUser, ]
        return super(PlansViewSet, self).get_permissions()

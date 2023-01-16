from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'service_app'

router = DefaultRouter()
router.register(r'', views.ServicesViewSet, basename='services')

urlpatterns = [
    path('', include(router.urls)),
]

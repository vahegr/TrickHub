from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'sample_app'

router = DefaultRouter()
router.register(r'', views.SamplesViewSet, basename='samples')

urlpatterns = [
    path('', include(router.urls)),
]

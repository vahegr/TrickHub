from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'about_app'

router = DefaultRouter()
router.register(r'', views.AboutsViewSet, basename='abouts')

urlpatterns = [
    path('', include(router.urls)),
]

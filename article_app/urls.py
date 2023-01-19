from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'article_app'

router = DefaultRouter()
router.register(r'', views.ArticleViewSet, basename='articles')

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path, include, re_path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'article_app'

urlpatterns = [
    path('', views.ArticlesView.as_view(), name='articles'),
    re_path(r'aricle_detail/(?P<id>[0-9]+)/(?P<slug>[-\w]+)/', views.ArticleDetailView, name='article_detail'),
]

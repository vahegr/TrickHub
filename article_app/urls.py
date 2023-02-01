from django.urls import path, include, re_path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'article_app'

urlpatterns = [
    path('', views.ArticlesView.as_view(), name='articles'),
    re_path(r'article_detail/(?P<id>[0-9]+)/(?P<slug>[-\w]+)/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article_update/<int:id>', views.UpdateArticleView.as_view(), name='article_update'),
    path('article_delete/<int:id>', views.DeleteArticleView.as_view(), name='article_update'),
    path('like/<int:id>', views.LikeListCreate.as_view(), name='article_like'),
]

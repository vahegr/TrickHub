from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'plan_app'

router = DefaultRouter()
router.register(r'', views.PlansViewSet, basename='plans')

urlpatterns = [
    path('', include(router.urls)),
]

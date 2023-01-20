from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'contact_app'

router = DefaultRouter()
router.register(r'', views.ContactsViewSet, basename='contacts')

urlpatterns = [
    path('', include(router.urls)),
]

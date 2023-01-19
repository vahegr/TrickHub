from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from TrickHub import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account_app.urls')),
    path('services/', include('service_app.urls')),
    path('articles/', include('article_app.urls')),
    path('plans/', include('plan_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

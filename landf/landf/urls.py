from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.lostandfound.urls')),
    path('account/', include('backend.accounts.urls')),
    path('dashboard/', include('backend.dashboard.urls')),
    path('newsfeeds/', include('backend.newsfeeds.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

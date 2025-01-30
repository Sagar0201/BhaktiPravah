from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bhakti.urls')),  # Include the app's URLs
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': production.MEDIA_ROOT}),
]
# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
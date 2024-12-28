from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('llanquiPageApp.urls')),
]
# Configuración para servir archivos multimedia en desarrollo
if settings.DEBUG:  # Solo en modo DEBUG
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
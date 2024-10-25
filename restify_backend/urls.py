# restify_backend/urls.py
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # Genera el esquema de la API
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Documentación en Swagger UI en la raíz
    path('api/docs/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),  # Documentación en Redoc
]

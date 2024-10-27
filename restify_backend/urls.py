from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView, 
    SpectacularRedocView,
    SpectacularSwaggerView, 
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from sleep_management.views import (
    RegisterUserView,
    SleepDataViewSet,
    UserPreferencesViewSet, 
)


router = DefaultRouter()
router.register(r'user-preferences', UserPreferencesViewSet, basename='userpreferences')
router.register(r'sleep-data', SleepDataViewSet, basename='sleepdata')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterUserView.as_view(), name='register'),
]

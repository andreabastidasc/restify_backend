from rest_framework import viewsets
from .models import UserPreferences, SleepData
from .serializers import UserPreferencesSerializer, SleepDataSerializer


class UserPreferencesViewSet(viewsets.ModelViewSet):
    queryset = UserPreferences.objects.all()
    serializer_class = UserPreferencesSerializer

class SleepDataViewSet(viewsets.ModelViewSet):
    queryset = SleepData.objects.all()
    serializer_class = SleepDataSerializer

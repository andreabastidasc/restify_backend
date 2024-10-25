from rest_framework import serializers
from .models import UserPreferences, SleepData

class UserPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreferences
        fields = '__all__'

class SleepDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepData
        fields = '__all__'

from django.db import models
from django.contrib.auth.models import User

class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sleep_duration = models.IntegerField(default=8)
    use_smartwatch = models.BooleanField(default=False)

class SleepData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sleep_start = models.DateTimeField()
    sleep_end = models.DateTimeField(null=True, blank=True)
    data_source = models.CharField(max_length=100, choices=[('smartwatch', 'Smartwatch'), ('phone', 'Phone')])

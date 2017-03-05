from rest_framework import serializers
from .models import Alert


class AlertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alert
        fields = ('timestamp', 'sensor', 'home', 'notes')
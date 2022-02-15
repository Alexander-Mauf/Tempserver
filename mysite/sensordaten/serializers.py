from rest_framework import serializers

from . import models

class StandortSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Standort
        fields = '__all__'


class MesswertSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Messwert
        fields = '__all__'

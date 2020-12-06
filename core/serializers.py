from rest_framework import serializers

from .models import Sonda


class SondaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sonda
        fields = ['x', 'y', 'face']

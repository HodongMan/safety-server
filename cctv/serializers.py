from rest_framework import serializers

from .models import CCTV

class CCTVSerializer(serializers.ModelSerializer):

    class Meta:
        models = CCTV
        fields = (
            'management_agency',
            'street_address',
            'address',
            'installation_purpose',
            'camera_count',
            'camera_pixel',
            'shooting_direction',
            'keep_days',
            'installation_date',
            'latitude',
            'longitude',
            'base_date',
            'created',
            'modified',
        )
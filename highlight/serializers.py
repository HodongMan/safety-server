from rest_framework import serializers

from .models import (
    VideoInteraction,
    VideoHightlight,
)


class VideoInteractionSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoInteraction
        fields = (
            'pk',
            'video_id',
            'pointed_time',
            'created',
            'modified'
        )

class VideoHightlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoHightlight
        fields = (
            'pk',
            'video_id',
            'start_time',
            'end_time',
            'created',
            'modified',
        )

from rest_framework import serializers

from .models import CommentHighlight


class CommentHighlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentHighlight
        fields = (
            'pk',
            'video_id',
            'highlight_time',
            'is_active',
            'created',
            'modified'
        )
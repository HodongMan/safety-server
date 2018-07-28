import requests
import json
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import UserVideo, Video

YOUTUBE_KEY = 'AIzaSyBIpcZ0mcSonw0RLAqRw_GTWiFNiWK2fEQ'


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = (
            'pk',
            'video_id',
            'title',
            'description',
            'thumbnails',
            'publishedAt',
            'created',
            'modified'
        )

class UserVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserVideo
        fields = (
            'pk',
            'video_id',
            'is_active',
            'order',
            'favorite',
            'created',
            'modified',
        )

    def create(self, validated_data):
        
        video_id = validated_data['video_id']
        try:
            video_info = Video.objects.get(video_id=video_id)
        except:
            URL = 'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={0}&key={1}'.format(video_id, YOUTUBE_KEY)
            response = requests.get(URL)
            result = json.loads(response.text)
            video_info = result['items'][0]['snippet']
            Video(video_id=video_id, title=video_info['title'], description=video_info['description'], publishedAt=video_info['publishedAt'], thumbnails=video_info['thumbnails']['default']['url']).save()
        return UserVideo.objects.create(**validated_data)

class UserVideoJoinSerializer(serializers.Serializer):

    user = serializers.CharField(max_length=255)
    video_id = serializers.CharField(max_length=255)
    is_active = serializers.BooleanField()
    order = serializers.IntegerField()
    favorite = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    created = serializers.DateTimeField()
    modified = serializers.DateTimeField()
    thumbnails = serializers.CharField()
    publishedAt = serializers.DateTimeField()

    class Meta:
        model = UserVideo
        fields = (
            'pk',
            'video_id',
            'is_active',
            'order',
            'favorite',
            'created',
            'modified',
        )

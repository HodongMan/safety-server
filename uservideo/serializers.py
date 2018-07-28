import requests
import json
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import UserVideo, Video

YOUTUBE_KEY = 'AIzaSyBIpcZ0mcSonw0RLAqRw_GTWiFNiWK2fEQ'


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
            'modified'
        )

    def create(self, validated_data):
        
        video_id = validated_data['video_id']
        try:
            video_info = Video.objects.get(video_id=video_id)
        except:
            URL = 'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={0}&key={1}'.format(video_id, YOUTUBE_KEY)
            response = requests.get(URL)
            result = json.loads(response.text)
            print(URL)
        return UserVideo.objects.create(**validated_data)

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
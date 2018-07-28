import requests
import json

from rest_framework import generics

from .models import UserVideo, Video
from .serializers import UserVideoSerializer, VideoSerializer, UserVideoJoinSerializer

YOUTUBE_KEY = 'AIzaSyBIpcZ0mcSonw0RLAqRw_GTWiFNiWK2fEQ'

class UserVideoList(generics.ListCreateAPIView):

    queryset = UserVideo.objects.all()
    serializer_class = UserVideoSerializer
    name = 'user-video-list'

class UserVideoJoinList(generics.ListAPIView):

    queryset = UserVideo.objects.all()
    serializer_class = UserVideoJoinSerializer
    name = 'user-video-join-list'

    def get_queryset(self):

        return UserVideo.objects.raw('select * from uservideo left join video on uservideo.video_id = video.video_id')

class UserVideoDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = UserVideo.objects.all()
    serializer_class = UserVideoSerializer
    name = 'user-video-detail'

class UserVideoListByUser(generics.ListCreateAPIView):

    queryset = UserVideo.objects.all()
    serializer_class = UserVideoSerializer
    name = 'user-video-list-by-user'

    def get_queryset(self):

        return UserVideo.objects.filter(self.kwargs['user'])

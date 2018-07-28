import requests
import json

from rest_framework import generics

from .models import UserVideo, Video
from .serializers import UserVideoSerializer, VideoSerializer

YOUTUBE_KEY = 'AIzaSyBIpcZ0mcSonw0RLAqRw_GTWiFNiWK2fEQ'

class UserVideoList(generics.ListCreateAPIView):

    queryset = UserVideo.objects.all()
    serializer_class = UserVideoSerializer
    name = 'user-video-list'

    def get_object(self, pk):

        video_info = Video.objects.get(video_id=self.kwargs['video_id'])
        print(video_id=self.kwargs['video_id'])
        return UserVideo.objects.get(pk=pk)
    
    def pre_save(self, obj):
        print('HAHAHAHAHAHAHA')


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

import requests
import json

from rest_framework import generics

from .models import UserVideo
from .serializers import UserVideoSerializer

YOUTUBE_KEY = 'AIzaSyBIpcZ0mcSonw0RLAqRw_GTWiFNiWK2fEQ'

class UserVideoList(generics.ListCreateAPIView):

    queryset = UserVideo.objects.all()
    serializer_class = UserVideoSerializer
    name = 'user-video-list'

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

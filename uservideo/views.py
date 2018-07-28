from rest_framework import generics

from .models import UserVideo
from .serializers import UserVideoSerializer

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

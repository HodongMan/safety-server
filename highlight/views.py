from rest_framework import generics

from .models import (
    VideoInteraction,
    VideoHightlight
)
from .serializers import (
    VideoInteractionSerializer,
    VideoHightlightSerializer,
)


class VideoInteractionList(generics.ListCreateAPIView):

    queryset = VideoInteraction.objects.all()
    serializer_class = VideoInteractionSerializer
    name = 'video-interaction-list'

class VideoInteractionDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = VideoInteraction.objects.all()
    serializer_class = VideoInteractionSerializer
    name = 'video-interaction-detail'

class VideoHightlightList(generics.ListCreateAPIView):

    queryset = VideoHightlight.objects.all()
    serializer_class = VideoHightlightSerializer
    name = 'video-hightlight-list'

class VideoHighlightDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = VideoHightlight.objects.all()
    serializer_class = VideoHightlightSerializer
    name = 'video-hightlight-detail'



import numpy as np
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

class ResponseHighlightSet(generics.ListAPIView):

    serializer_class = VideoHightlightSerializer
    name = 'responsehighlight-videoid-list'

    def get_queryset(self):

        video_id = self.kwargs['videoid']
        response_list = VideoInteraction.objects.filter(video_id=video_id)
        pointed_time_list = [item.pointed_time for item in response_list]
        VideoInteraction.objects.filter(video_id=video_id).delete()

        resp = makeHistogramByResponseTime(video_id, pointed_time_list)
        VideoHightlight.objects.bulk_create(resp)
        return VideoHightlight.objects.filter(video_id=video_id)

def makeHistogramByResponseTime(video_id, pointed_time_list):

    hist, bin_edges = np.histogram(pointed_time_list)
    average = sum(hist) / len(hist)

    resp = []
    for item, value in zip(hist, bin_edges):
        if item >= average:
            temp = VideoHightlight(video_id=video_id, start_time=value, end_time=value)
            resp.append(temp)

    return resp


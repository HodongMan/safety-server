import numpy as np
import random

from django.http import HttpResponse
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

class VidoeHightlightByVideo(generics.ListAPIView):

    queryset = VideoHightlight.objects.all()
    serializer_class = VideoHightlightSerializer
    name = 'video-hightlight-list-by-video'

    def get_queryset(self):

        video_id = self.kwargs['video']
        return VideoHightlight.objects.filter(video_id=video_id)


class ResponseHighlightSet(generics.ListAPIView):

    serializer_class = VideoHightlightSerializer
    name = 'responsehighlight-videoid-list'

    def get_queryset(self):

        video_id = self.kwargs['video']
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

def ResponseHighlightTestDataList(request):

    """
        # 해당 View는 테스트 결과를 임의로 생성
        # 혹은 테스트 결과에 필요한 샘플 데이터를 임의로 생성하는 역할
    """
    sample1 = [random.randint(30, 100) + random.random() for _ in range(500)]
    sample2 = [random.randint(150, 250) + random.random() for _ in range(500)]
    sample3 = [random.randint(400, 500) + random.random() for _ in range(500)]
    sample4 = [random.randint(600, 700) + random.random() for _ in range(500)]
    sample5 = [random.randint(730, 800) + random.random() for _ in range(500)]
    #sample6 = [random.randint(0, 800) + random.random() for _ in range(3000)]

    y_data = sample1 + sample2 + sample3 + sample4 + sample5

    hist, bin_edges = np.histogram(y_data)

    average = sum(hist) / len(hist)
    resp = []
    for item, value in zip(hist, bin_edges):
        if item >= average:
            resp.append(value)

    #sample_data = []

    #for item in y_data:
        #sample_data.append(Response(video_id='gQTQxEp7OLc', pointed_time=item))
    #print(len(sample_data))

    #Response.objects.bulk_create(sample_data)


    result = " ".join(str(txt) for txt in resp)

    return HttpResponse(result)
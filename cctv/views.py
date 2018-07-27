from rest_framework import generics

from .models import CCTV
from .serializers import CCTVSerializer


class CCTVList(generics.ListCreateAPIView):

    queryset = CCTV.objects.all()
    serializer_class = CCTVSerializer
    name = 'cctv-list'

class CCTVDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = CCTV.objects.all()
    serializer_class = CCTVSerializer
    name = 'cctv-detail'


import requests
import json

from rest_framework import generics

from .models import CommentHighlight
from .serializers import CommentHighlightSerializer


YOUTUBE_KEY = 'AIzaSyBIpcZ0mcSonw0RLAqRw_GTWiFNiWK2fEQ'

class CommentHighlightList(generics.ListCreateAPIView):

    queryset = CommentHighlight.objects.all()
    serializer_class = CommentHighlightSerializer
    name = 'comment-highlight-list'

class CommentHighlightDetail(generics.ListCreateAPIView):

    queryset = CommentHighlight.objects.all()
    serializer_class = CommentHighlightSerializer
    name = 'comment-highlight-detail'


def getCommentParsingResult(video_id):

    video_id = '0wlXaHmmOVc'
    URL = 'https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={0}&key={1}&maxResults={2}'.format(video_id, YOUTUBE_KEY, 20)
    response = requests.get(URL)
    
    result = json.loads(response.text)
    
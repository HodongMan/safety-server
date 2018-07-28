import requests
import json
import re

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


class getCommentParsingResult(generics.ListAPIView):
    
    serializer_class = CommentHighlightSerializer
    name = 'responsehighlight-comment-list'

    def get_queryset(self):
        
        video_id = self.kwargs['video']
        URL = 'https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={0}&key={1}&maxResults={2}'.format(video_id, YOUTUBE_KEY, 100)
        response = requests.get(URL)
        result = json.loads(response.text)
        time_result = set([])
        
        for item in result['items']:
            display_text = item['snippet']['topLevelComment']['snippet']['textDisplay']
            text_index = display_text.find('</a>')
            
            if 0 < text_index:
                for match in re.finditer('([0-5]?[0-9]):([0-5]?[0-9])', display_text, re.S):
                    time_result.add(match.group(0))
                    print(match.group(0))

        result_list = []
        for item in time_result:
            result_list.append(CommentHighlight(video_id=video_id, highlight_time=item))
            print(item)

        CommentHighlight.objects.filter(video_id=video_id).delete()
        CommentHighlight.objects.bulk_create(result_list)
        return CommentHighlight.objects.filter(video_id=video_id)

        
    
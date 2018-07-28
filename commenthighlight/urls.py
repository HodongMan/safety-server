from django.urls import path

from .views import (
    CommentHighlightList,
    CommentHighlightDetail,
    getCommentParsingResult
)


urlpatterns = [
    path("", CommentHighlightList.as_view(), name = CommentHighlightList.name),
    path("<int:pk>/", CommentHighlightDetail.as_view(), name = CommentHighlightDetail.name),
    path('video/<str:video>', getCommentParsingResult.as_view(), name = getCommentParsingResult.name),
]
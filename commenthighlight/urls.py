from django.urls import path

from .views import (
    CommentHighlightList,
    CommentHighlightDetail
)


urlpatterns = [
    path("", CommentHighlightList.as_view(), name = CommentHighlightList.name),
    path("<int:pk>/", CommentHighlightDetail.as_view(), name = CommentHighlightDetail.name),
]
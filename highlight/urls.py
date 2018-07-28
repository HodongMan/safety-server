from django.urls import path

from .views import (
    VideoInteractionList,
    VideoInteractionDetail,
    VideoHightlightList,
    VideoHighlightDetail,
    VidoeHightlightByVideo,
    ResponseHighlightTestDataList,
    ResponseHighlightSet,
)

urlpatterns = [
    path("", VideoHightlightList.as_view(), name = VideoHightlightList.name),
    path("<int:pk>/", VideoHighlightDetail.as_view(), name = VideoHighlightDetail.name),
    path("video/<str:video>", VidoeHightlightByVideo.as_view(), name = VidoeHightlightByVideo.name),
    path("interaction", VideoInteractionList.as_view(), name = VideoInteractionList.name),
    path("interaction/<int:pk>/", VideoInteractionDetail.as_view(), name = VideoInteractionDetail.name),
    path("test/", ResponseHighlightTestDataList, name = 'response-test-list'),
    path("set/<str:video>/", ResponseHighlightSet.as_view(), name = ResponseHighlightSet.name),
]
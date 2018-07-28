from django.urls import path

from .views import (
    VideoInteractionList,
    VideoInteractionDetail,
    VideoHightlightList,
    VideoHighlightDetail,
)


urlpatterns = [
    path("", VideoHightlightList.as_view(), name = VideoHightlightList.name),
    path("<int:pk>/", VideoHighlightDetail.as_view(), name = VideoHighlightDetail.name),
    path("interaction", VideoInteractionList.as_view(), name = VideoInteractionList.name),
    path("interaction/<int:pk>/", VideoInteractionDetail.as_view(), name = VideoInteractionDetail.name),
]
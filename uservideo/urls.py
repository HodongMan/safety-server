from django.urls import path

from .views import (
    UserVideoList,
    UserVideoDetail,
    UserVideoListByUser,
)


urlpatterns = [
    path("", UserVideoList.as_view(), name = UserVideoList.name),
    path("<int:pk>/", UserVideoDetail.as_view(), name = UserVideoDetail.name),
    path("user/<str:user>", UserVideoListByUser.as_view(), name = UserVideoListByUser.name),
]